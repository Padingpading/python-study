import threading
# ========== args 参数 ==========
# 1、引入
#    target 只接收「函数对象」，真正调用时还需要参数。
#    若把参数写死在函数里，复用性差；所以用 args 把位置参数交给线程。
#    例：同一 people 函数，可开多个线程分别传 ("张三",20)、("李四",18)。
# 2、定义
#    概念：传给 target 的位置参数。
#    形式：必须是元组/列表，默认 ()。
#          Thread(target=fn, args=("A", 2))  →  内部执行 fn("A", 2)
# 3、使用
def people(name, age):
    print(f"{name},{age}岁了")
t = threading.Thread(target=people, args=("张三", 20))          
# 启动前打印：内部字段是 _args，没有公开的 .args 属性（不像 name 有 @property）
print(f"args: {t._args}")
t.start()
# 特点
#    - 按位置顺序对应 target 形参   
#    - 单元素也要写成元组：args=("张三",)  不能写成 args=("张三")   
#    - 与 kwargs 配合：位置参数用 args，关键字参数用 kwargs
# 注意点
#    1. 对外没有 t.args，只有内部 t._args（约定：不依赖私有字段写业务）
#    2. run() 结束后会 del self._args，线程跑完后再读可能 AttributeError
#    3. args 必须可迭代；传单个字符串会按字符拆开：args="张三" → target("张","三")

#单个参数（元组逗号不能省略）
def work(num):
    print(f"数字：{num}")
# 单参数元组末尾必须加 ,
t = threading.Thread(target=work, args=(100,))
t.start()

#多位置参数场景
def work_multi_info(username, user_age):
    print(f"用户姓名：{username}，年龄：{user_age}")

t2 = threading.Thread(target=work_multi_info, args=("张三", 22))
t2.start()
#args + kwargs 混合传参（位置 + 关键字参数）
def work_mix_calc(a, b, offset=0):
    res = a + b + offset
    print(f"混合计算结果：{res}")
t3 = threading.Thread(target=work_mix_calc, args=(1, 2), kwargs={"offset": 3})
t3.start()
#循环批量创建多线程传参
def work_loop_serial(thread_index):
    print(f"批量线程编号：{thread_index}")
thread_list = []
for i in range(3):
    t = threading.Thread(target=work_loop_serial, args=(i,))
    thread_list.append(t)
    t.start()

#注意点1:args 仅用于向线程函数传入参数，线程函数 return 的返回值不会回填到 args，会直接被 Python 解释器丢弃，下面先看错误示范，再给三种可行方案（均使用 args 传参）
def task_test_return(a, b):
    return a + b  # 返回值会直接丢弃
    # args 只是传入参数，不会接收函数返回结果
args_tuple = (10, 20)
t = threading.Thread(target=task_test_return, args=args_tuple)
t.start()
t.join()
print(args_tuple)  # 输出 (10, 20)，args 没有任何变化，拿不到30