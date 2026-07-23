# =============================================================================
# Python 标准库 threading.Thread 源码中文精读
# 来源：CPython Lib/threading.py（Python 3.14 附近）
# 目的：理解 Thread 对象如何从「创建」到「启动」再到「结束」
#
# 【整体执行链路】（对应你写的 Thread(target=task).start()）
#   1. __init__          ：只创建 Thread 对象，还没真正开系统线程
#   2. start()           ：向 OS 申请新线程，入口设为 _bootstrap
#   3. _bootstrap        ：新线程里的外壳，处理解释器退出时的异常
#   4. _bootstrap_inner  ：登记线程身份，再调用 run()
#   5. run()             ：真正执行你传入的 target(*args, **kwargs)
#   6. _delete / join    ：清理活动表 / 主线程等待子线程结束
#
# 【两种指定线程任务的方式】
#   方式A：Thread(target=函数, args=(...))  —— 最常用
#   方式B：继承 Thread，重写 run()          —— 面向对象写法
# =============================================================================


class Thread:
    """表示一条「控制流线程」的类（不是 OS 线程本身，而是其 Python 封装）。

    可以有限地安全子类化。指定线程要做什么，有两种方式：
      1. 构造时传入可调用对象 target
      2. 子类中重写 run() 方法
    """

    # 类属性默认 False。实例 __init__ 成功结束时会改成 True。
    # 作用：防止子类忘了调用 Thread.__init__() 就去 start()/join()，
    # 否则内部属性未初始化会出诡异错误。
    _initialized = False

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None, context=None):
        """构造 Thread 对象（注意：此时还没有真正启动线程！）。

        官方建议尽量用关键字传参，可读性更好，也避免参数位置搞错。

        参数说明：
        *group*
            目前必须是 None。预留给将来的 ThreadGroup（线程组）扩展，
            现在传别的会直接 assert 失败。

        *target*
            线程真正要执行的可调用对象（函数/方法/可调用对象）。
            默认 None：run() 里什么都不调（适合子类自己重写 run）。

        *name*
            线程名字，仅用于标识/调试，没有特殊语义。
            默认类似 "Thread-1 (task)"，方便在日志里区分。

        *args*
            传给 target 的位置参数，必须是元组/列表，默认 ()。
            例：args=("A", 2)  →  target("A", 2)

        *kwargs*
            传给 target 的关键字参数字典，默认 {}。
            例：kwargs={"sleep_time": 2} → target(sleep_time=2)

        *daemon*
            是否守护线程。True：主程序只剩守护线程时也会退出；
            False：主程序会等它跑完（非守护线程会拖住进程退出）。
            默认 None：继承「创建它的那个线程」的 daemon 属性。
            主线程 daemon=False，所以主线程里新建的线程默认也是 False。

        *context*
            contextvars.Context，决定新线程里上下文变量怎么继承。
            None 时看 sys.flags.thread_inherit_context：
              - True  → 复制调用方上下文
              - False → 空上下文
            也可手动传 Context() 或 copy_context() 的结果。

        子类若重写 __init__，必须先调用 Thread.__init__()，
        再做自己的事，否则 _initialized 仍为 False，start 会报错。
        """
        # group 预留参数：现在尚未实现 ThreadGroup，传非 None 直接断言失败
        assert group is None, "group argument must be None for now"

        # kwargs 默认写成 None 再在这里变 {}，是为了避免：
        #   def f(kwargs={}): ...  这种「可变默认参数」陷阱
        # （若用 kwargs={} 写在形参里，多次调用会共享同一个 dict）
        if kwargs is None:
            kwargs = {}

        # ----- 生成线程名 -----
        if name:
            # 用户指定了名字：统一转成 str，保证后续比较/打印安全
            name = str(name)
        else:
            # 自动生成唯一名：Thread-1、Thread-2 ...
            name = _newname("Thread-%d")
            if target is not None:
                # 若 target 有 __name__（普通函数有），追加到名字里
                # 例：Thread-1 (task)，调试时一眼看出在跑哪个函数
                try:
                    target_name = target.__name__
                    name += f" ({target_name})"
                except AttributeError:
                    # 某些可调用对象没有 __name__（如 lambda/自定义对象），忽略即可
                    pass

        # ----- 保存「稍后在子线程里执行」所需的信息 -----
        # start() 之前这些只是普通属性；真正调用发生在 run() 里
        self._target = target          # 要执行的函数
        self._name = name              # 线程名
        self._args = args              # 位置参数
        self._kwargs = kwargs          # 关键字参数

        # ----- 守护线程属性 -----
        if daemon is not None:
            # 显式指定了 daemon
            if daemon and not _daemon_threads_allowed():
                # 某些子解释器禁止守护线程（资源/生命周期管理更严格）
                raise RuntimeError('daemon threads are disabled in this (sub)interpreter')
            self._daemonic = daemon
        else:
            # 未指定：继承当前线程（通常是主线程）的 daemon 值
            # 原因：父子线程属性保持一致，避免「主线程非守护、子线程却偷偷变守护」
            self._daemonic = current_thread().daemon

        self._context = context        # 上下文；真正确定值多半在 start() 里
        self._ident = None             # Python 层线程 id，启动前未知

        # 部分平台支持「原生线程 ID」（操作系统内核里的 TID）
        if _HAVE_THREAD_NATIVE_ID:
            self._native_id = None

        # OS 层可 join 的线程句柄（底层封装），join()/is_alive() 都靠它
        self._os_thread_handle = _ThreadHandle()

        # Event：标记「线程是否已真正启动起来」
        # start() 末尾会 wait() 等它；_bootstrap_inner 里 set()
        # 作用：保证 start() 返回时，ident/native_id 已经可用
        self._started = Event()

        # 初始化完成标志：之后 start/join/属性访问才合法
        self._initialized = True

        # 拷贝一份 stderr，供异常钩子打印用
        # 原因：线程结束/解释器清理时，sys.stderr 可能已变 None，
        # 提前保存一份，避免「报错时连错误都打不出来」
        self._stderr = _sys.stderr

        # 生成「调用 threading.excepthook」的闭包，处理 run() 未捕获异常
        self._invoke_excepthook = _make_invoke_excepthook()

        # 挂到弱引用集合，便于调试和 fork 后清理
        # 原因：线程对象可能还没 start 就被遗弃，需要追踪这类「悬空」对象
        _dangling.add(self)

    def _after_fork(self, new_ident=None):
        # 私有方法！由 threading._after_fork() 在 os.fork() 之后调用。
        #
        # 背景：Unix 上 fork 只复制「当前线程」，其他线程在子进程里消失，
        # 但 Python 里可能还残留这些 Thread 对象，状态必须重置/修正。
        self._started._at_fork_reinit()  # 重置 Event 内部状态（锁等）

        if new_ident is not None:
            # 当前仍存活的线程（通常是 fork 那条）：更新成新进程里的 ident
            self._ident = new_ident
            assert self._os_thread_handle.ident == new_ident
            if _HAVE_THREAD_NATIVE_ID:
                self._set_native_id()
        else:
            # 其他线程在 fork 后已死：底层已把 handle 标为 done，这里无需再做事
            # （注释里 "the thread is dead, Jim" 是星际迷航梗）
            pass

    def __repr__(self):
        """调试用字符串表示，例：
        <Thread(Thread-1 (task), started 12345)>
        <Thread(Thread-2, stopped daemon)>
        """
        # 没调 __init__ 就 repr，直接断言，尽早暴露子类写法错误
        assert self._initialized, "Thread.__init__() was not called"

        # 状态机：initial → started → stopped
        status = "initial"
        if self._started.is_set():
            status = "started"
        if self._os_thread_handle.is_done():
            status = "stopped"
        if self._daemonic:
            status += " daemon"       # 守护线程额外标注
        if self._ident is not None:
            status += " %s" % self._ident  # 附带 Python 线程 id
        return "<%s(%s, %s)>" % (self.__class__.__name__, self._name, status)

    def start(self):
        """真正启动线程：让 OS 新建一条控制流，并在其中调用 run()。

        每个 Thread 对象最多只能 start 一次。
        重复 start 会 RuntimeError（系统线程不能「复活」同一个对象）。

        注意：
        - 调用 start() 的通常是主线程
        - start() 返回后，子线程已经在并行跑了（或马上会跑）
        - start() 内部会短暂阻塞，直到子线程完成身份登记（见末尾 wait）
        """
        # 子类忘调父类 __init__ → 属性不全，禁止启动
        if not self._initialized:
            raise RuntimeError("thread.__init__() not called")

        # 已启动过就不能再启：防止同一对象对应两条 OS 线程，状态混乱
        if self._started.is_set():
            raise RuntimeError("threads can only be started once")

        # 先放进「炼狱」字典 _limbo：
        # 含义：已决定启动，但还没在 _active 里正式登记。
        # 原因：从「调用 _start_joinable_thread」到「子线程写入 _active」之间
        # 有窗口期；enumerate() 等 API 需要能看到「正在启动中」的线程，
        # 否则可能短暂「丢线程」。
        with _active_limbo_lock:
            _limbo[self] = self

        # 若构造时没传 context，此时再决定继承策略
        # （放在 start 而不是 __init__：因为要按「启动瞬间」的调用方上下文来复制）
        if self._context is None:
            if _sys.flags.thread_inherit_context:
                # 复制启动者当前的 contextvars（如 request_id 等）
                self._context = _contextvars.copy_context()
            else:
                # 空上下文：子线程不继承调用方的上下文变量
                self._context = _contextvars.Context()

        try:
            # 关键底层：创建可 join 的系统线程
            # 新线程入口函数是 self._bootstrap（不是直接 run！）
            # handle：用来之后 join / 查是否结束
            # daemon：告诉底层这是不是守护线程
            _start_joinable_thread(self._bootstrap, handle=self._os_thread_handle,
                                   daemon=self.daemon)
        except Exception:
            # 创建系统线程失败：从 _limbo 移除，避免脏数据残留
            with _active_limbo_lock:
                del _limbo[self]
            raise

        # 阻塞等待：直到子线程在 _bootstrap_inner 里执行 self._started.set()
        # 原因：保证 start() 返回时，ident / native_id 已经设好，
        # 调用方立刻读 t.ident 不会拿到 None。
        self._started.wait()  # Will set ident and native_id

    def run(self):
        """线程的「业务入口」：真正要做的事情写在这里。

        - 传了 target：默认实现就调用 target(*args, **kwargs)
        - 子类重写 run()：就不依赖 target（继承写法）

        重要：run() 是在「子线程」里执行的，不是在调用 start() 的主线程里。
        对应源码：_bootstrap_inner → self._context.run(self.run)
        """
        try:
            if self._target is not None:
                # * / ** 解包：把构造时存的参数喂给 target
                # 这就是你写 Thread(target=task, args=("A", 2)) 能工作的核心
                self._target(*self._args, **self._kwargs)
        finally:
            # 主动删掉 target/args/kwargs 的引用
            # 原因：避免引用循环导致无法回收。
            # 典型场景：args 里某个对象持有 Thread 引用，而 Thread 又持有 args，
            # 形成环；del 断环，利于 GC。
            del self._target, self._args, self._kwargs

    def _bootstrap(self):
        # 新线程真正的「外壳入口」。
        # 不直接跑业务，而是包一层 _bootstrap_inner，专门处理：
        # 「解释器正在关闭时，守护线程醒来发现世界已毁」产生的噪音异常。
        #
        # 典型场景：
        #   主程序退出 → 解释器清理模块（sys 等变 None）
        #   守护线程还在跑 → _bootstrap_inner 里报错，甚至「报告错误时再报错」
        # 这些异常对用户没帮助，还吓人，所以在特定条件下吞掉。
        #
        # 只对「守护线程 + 解释器已毁（_sys is None）」静默；
        # 普通非守护线程若走到这里，说明更严重的问题，继续抛出。
        try:
            self._bootstrap_inner()
        except:
            if self._daemonic and _sys is None:
                return
            raise

    def _set_ident(self):
        """记录 Python 层线程标识（threading.get_ident()）。
        同一进程内唯一（线程结束后可能被复用）。
        """
        self._ident = get_ident()

    # 仅当平台提供原生 TID API 时，才定义该方法（条件定义）
    if _HAVE_THREAD_NATIVE_ID:
        def _set_native_id(self):
            """记录操作系统内核线程 ID（get_native_id()）。
            调试、对齐系统工具（如 top/htop）时很有用。
            """
            self._native_id = get_native_id()

    def _set_os_name(self):
        """把 Python 线程名同步到 OS 线程名（若平台支持）。
        方便在系统监视器里看到 "Thread-1 (task)" 而不是无意义名字。
        失败就忽略：名字只是锦上添花，不能因此让线程挂掉。
        """
        if _set_name is None or not self._name:
            return
        try:
            _set_name(self._name)
        except OSError:
            pass

    def _bootstrap_inner(self):
        """子线程启动后的「内部引导」：登记身份 → 执行 run → 清理。

        这是整条链路里最关键的一段，顺序很讲究：
        1. 设 ident / native_id / OS 名
        2. _started.set()  —— 唤醒主线程里 start() 的 wait()
        3. 从 _limbo 挪到 _active  —— 正式成为「活动线程」
        4. 安装 trace/profile 钩子（若有）
        5. 在指定 context 中执行 run()
        6. 无论成功失败，finally 里 _delete() 从活动表移除
        """
        try:
            # 1) 身份信息：必须在本线程内获取（get_ident 返回「当前」线程）
            self._set_ident()
            if _HAVE_THREAD_NATIVE_ID:
                self._set_native_id()
            self._set_os_name()

            # 2) 通知 start()：我已经起来了，ident 可读了
            self._started.set()

            # 3) 活动线程登记：_active[ident] = self；同时离开 _limbo
            # 加锁：与 enumerate()/current_thread() 等共享字典，避免竞态
            with _active_limbo_lock:
                _active[self._ident] = self
                del _limbo[self]

            # 4) 调试钩子：让新线程也继承全局的 trace/profile 设置
            if _trace_hook:
                _sys.settrace(_trace_hook)
            if _profile_hook:
                _sys.setprofile(_profile_hook)

            try:
                # 5) 在绑定好的 contextvars.Context 中执行 run()
                # 用 context.run(self.run) 而不是直接 self.run()，
                # 是为了保证 contextvars 在该线程内正确生效。
                self._context.run(self.run)
            except:
                # run() 里未捕获异常：不直接让线程「静默死掉」，
                # 而是走 excepthook，打印堆栈（默认打到 stderr）
                self._invoke_excepthook(self)
        finally:
            # 6) 无论正常结束还是异常，都要从活动表删除
            # 否则 enumerate() 会一直看到「已死线程」
            self._delete()

    def _delete(self):
        """从「当前正在运行的线程」字典 _active 中移除自己。"""
        with _active_limbo_lock:
            del _active[get_ident()]
            # 锁释放前不要再跑别的 Python 代码！
            # 原因：若中间触发了 tracing，tracing 里可能再调 current_thread()，
            # 又试图获取同一把锁 → 同线程重入死锁。

    def join(self, timeout=None):
        """阻塞「调用 join 的线程」，直到「被 join 的线程」结束。

        常见用法：主线程 start 多个子线程后，逐个 join，确保都做完再继续。

        *timeout*
            None：一直等到对方结束。
            数字（秒）：最多等这么久；超时也返回 None。
            要判断是否超时：join 后看 is_alive()，仍为 True 就是超时。

        可多次 join 同一个线程（已结束再 join 会立刻返回）。

        禁止：
        - join 自己（会死锁：永远等自己结束）
        - 线程还没 start 就 join
        """
        if not self._initialized:
            raise RuntimeError("Thread.__init__() not called")
        if not self._started.is_set():
            raise RuntimeError("cannot join thread before it is started")
        if self is current_thread():
            # 自己等自己：逻辑死锁，直接拒绝
            raise RuntimeError("cannot join current thread")

        # 负超时历史上按 0 处理（立刻检查是否已结束），保持兼容
        if timeout is not None:
            timeout = max(timeout, 0)

        # 真正等待交给 OS 层线程句柄（可被中断/带超时）
        self._os_thread_handle.join(timeout)

    @property
    def name(self):
        """线程名：仅标识用，无特殊语义；多个线程可以同名。"""
        assert self._initialized, "Thread.__init__() not called"
        return self._name

    @name.setter
    def name(self, name):
        assert self._initialized, "Thread.__init__() not called"
        self._name = str(name)
        # 若「当前正在跑的就是这个线程」，立刻把新名字同步到 OS
        # （别的线程改名字：等不到本线程自己去 _set_os_name 的时机，
        #  这里只能改 Python 层 _name；本线程内改名则可同步 OS）
        if get_ident() == self._ident:
            self._set_os_name()

    @property
    def ident(self):
        """Python 线程标识；未启动为 None。
        非零整数；线程退出后仍可读取；id 可能被后续新线程复用。
        """
        assert self._initialized, "Thread.__init__() not called"
        return self._ident

    if _HAVE_THREAD_NATIVE_ID:
        @property
        def native_id(self):
            """操作系统内核报告的线程 ID；未启动为 None。
            与 ident（Python 层）不同：这是内核 TID。
            """
            assert self._initialized, "Thread.__init__() not called"
            return self._native_id

    def is_alive(self):
        """线程是否仍存活。

        True 的大致区间：run() 即将开始 → run() 刚结束。
        实现：已 start，且 OS 句柄尚未标记完成。
        """
        assert self._initialized, "Thread.__init__() not called"
        return self._started.is_set() and not self._os_thread_handle.is_done()

    @property
    def daemon(self):
        """是否守护线程。

        必须在 start() 之前设置，启动后改会 RuntimeError。
        默认继承创建者；主线程非守护 → 主线程创建的线程默认也非守护。

        关键点规则：
          当只剩下守护线程时，整个 Python 进程可以退出
         （守护线程会被强制结束，不一定跑完）。
        """
        assert self._initialized, "Thread.__init__() not called"
        return self._daemonic

    @daemon.setter
    def daemon(self, daemonic):
        if not self._initialized:
            raise RuntimeError("Thread.__init__() not called")
        if daemonic and not _daemon_threads_allowed():
            raise RuntimeError('daemon threads are disabled in this interpreter')
        # 已启动就不能改：守护属性影响进程退出策略，中途改会语义混乱
        if self._started.is_set():
            raise RuntimeError("cannot set daemon status of active thread")
        self._daemonic = daemonic

    # -------------------------------------------------------------------------
    # 以下旧式 Java 风格 getter/setter：仅为兼容老代码，已废弃
    # 新代码请直接用：t.daemon / t.name 属性
    # -------------------------------------------------------------------------

    def isDaemon(self):
        """已废弃：请用 t.daemon 属性。"""
        import warnings
        warnings.warn('isDaemon() is deprecated, get the daemon attribute instead',
                      DeprecationWarning, stacklevel=2)
        return self.daemon

    def setDaemon(self, daemonic):
        """已废弃：请用 t.daemon = ..."""
        import warnings
        warnings.warn('setDaemon() is deprecated, set the daemon attribute instead',
                      DeprecationWarning, stacklevel=2)
        self.daemon = daemonic

    def getName(self):
        """已废弃：请用 t.name 属性。"""
        import warnings
        warnings.warn('getName() is deprecated, get the name attribute instead',
                      DeprecationWarning, stacklevel=2)
        return self.name

    def setName(self, name):
        """已废弃：请用 t.name = ..."""
        import warnings
        warnings.warn('setName() is deprecated, set the name attribute instead',
                      DeprecationWarning, stacklevel=2)
        self.name = name


# =============================================================================
# 【对照你的示例：函数传参.py】
#
#   t1 = threading.Thread(target=task, args=("A", 2))
#   # → __init__：保存 _target=task, _args=("A",2)，尚未开线程
#
#   t1.start()
#   # → start：OS 开新线程，入口 _bootstrap → _bootstrap_inner → run
#   # → run：task(*("A", 2)) 即 task("A", 2) 在子线程执行
#
#   t1.join()
#   # → 主线程阻塞，直到 t1 的 OS 线程结束
#
# 【关键记忆】
#   Thread 对象 ≠ 立刻有 OS 线程
#   start() 才真正创建 OS 线程
#   run()/target 跑在子线程；start()/join() 通常跑在主线程
# =============================================================================
