import threading
import time

#  def __init__(self, group=None, target=None, name=None,  args=(), kwargs=None, *, daemon=None, context=None):
# group:

# 定义线程的执行入口：指定线程并发运行的业务代码，是线程的逻辑主体；
# 配合 args /kwargs 完成参数传递：target 只负责接收函数对象，参数通过另外两个参数传入；
# 区分两种线程写法：
# 传入 target：函数式创建线程，轻量化；
# 不传入 target（target=None）：必须重写 run() 方法，面向对象自定义线程；
# 线程生命周期绑定 target：target 函数执行完毕，线程正常退出；函数内部异常，线程终止并打印堆栈。

def sayHello():
    print("多线程执行")
t = threading.Thread(target=sayHello(),args=("A", 2))
t.start()

# lambda 匿名函数
t = threading.Thread(target=lambda: print("lambda 线程执行"))
t.start()

# 类实例方法
class Task:
    def run_task(self, msg):
        print(msg)
        time.sleep(1)

obj = Task()
# 传入实例方法
t = threading.Thread(target=obj.run_task, args=("实例方法线程",))
t.start()

#实现 call 的类实例
class CallTask:
    def __call__(self, text):
        print(f"可调用对象执行：{text}")
t = threading.Thread(target=CallTask(), args=("测试",))
t.start()
#__call__ 在对象调用  obj() 时候会默认调用这个方法
#例如:CallTask()("五点")
