import threading
import time

# 全局只创建一个local实例
ctx = threading.local()
# 获取。
def worker(val):
    # 给当前线程上下文绑定属性
    ctx.data = val
    time.sleep(0.1)
    # 判断是否封存在属性
    if hasattr(ctx,"data"):
        print("存在属性")

    print(f"线程{threading.get_ident()}, ctx.data = {ctx.data}")
t1 = threading.Thread(target=worker, args=[100])
t2 = threading.Thread(target=worker, args=[200])
t1.start()
t2.start()
t1.join()


#初始化钩子（init 线程私有初始化）
class MyContext(threading.local):
    def __init__(self):
        # ⚠️注意：仅在线程第一次访问该实例时执行一次
        self.trace_id = None
ctx = MyContext()

# 特点
# 数据隔离：同一个 local 实例，不同线程访问得到相互独立的属性空间。
# 实例全局唯一即可：不需要每个线程新建 local 对象，全局单例足够。
# 懒创建：属性只有赋值后才会在当前线程上下文生成。
# 不自动继承：主线程上下文数据不会默认拷贝到子线程。
# 依附线程生命周期：线程销毁后，该线程对应的本地数据自动被垃圾回收。
# 存取速度快：底层 C 实现，性能远高于手动维护 {thread_id: data} 字典。
# 不能在线程间传递上下文数据,设计初衷就是隔离；如果需要跨线程共享数据，要用队列、全局锁、显式传参，不要依赖 local。
# 属性访问不存在会抛 AttributeError,读取未赋值的属性直接报错，建议先用 hasattr() 判断或者设置默认值。
# threading.local() 无法自动传递到子线程 Web 框架（FastAPI/Flask）上下文传递一般框架内部做了封装；原生 Python 多线程必须手动把上下文变量传给子线程。
# 不要存储大对象、锁资源线程 大量创建销毁时，虽然 GC 会回收，但频繁创建超大上下文对象会增加内存压力；禁止在线程上下文中持有互斥锁，极易引发逻辑混乱。
# 不兼容 multiprocessing 多进程 TLS 仅作用于同一进程内的线程；进程之间内存隔离，local 失效。
# 协程场景（asyncio）不要混用 threading.local，asyncio 使用单线程多路复用，多个协程共用同一个线程，会造成上下文互相覆盖。协程上下文应当使用 contextvars（Python3.7+