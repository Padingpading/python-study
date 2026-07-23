import threading
import time

# 普通顶层函数
def sayHello(name,age):
    print("普通顶层函数")
t = threading.Thread(target=sayHello,args=("A", 2))
t.start()

# lambda 匿名函数
t = threading.Thread(target=lambda: print("lambda 线程执行"))
t.start()

# 类:实例方法
class Task:
    def run_task(self, msg):
        print(msg)
        time.sleep(1)

obj = Task()
# 传入实例方法
t = threading.Thread(target=obj.run_task, args=("实例方法线程",))
t.start()
# 类 @staticmethod 静态方法
class StaticTask:
    @staticmethod
    def run_task(msg):
        print(msg)
        time.sleep(1)

# 静态方法不依赖实例，可直接通过类传入
t = threading.Thread(target=StaticTask.run_task, args=("静态方法线程",))
t.start()   

# 类 @classmethod 类方法
class ClassTask:
    @classmethod
    def run_task(cls, msg):
        print(f"{cls.__name__}: {msg}")
        time.sleep(1)

# 类方法第一个参数是 cls，线程只会额外传入 args 里的参数
t = threading.Thread(target=ClassTask.run_task, args=("类方法线程",))
t.start()

#类:实现 call 的类实例
class CallTask:
    def __call__(self, text):
        print(f"可调用对象执行：{text}")
t = threading.Thread(target=CallTask(), args=("测试",))
t.start()
#__call__ 在对象调用  obj() 时候会默认调用这个方法
#例如:CallTask()("五点")
