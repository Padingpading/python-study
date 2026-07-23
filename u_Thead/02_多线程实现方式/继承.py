import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
      # 父类初始化，必须第一行
        super().__init__()  # 必须调用父类构造
        # 传参通过实例属性存储，不用 args/kwargs。
        self.name = name
        self.delay = delay
    # 必须重写 run() 方法，run 内部是线程业务逻辑；
    def run(self):
        # 线程核心业务逻辑
        print(f"自定义线程 {self.name} 开始运行")
        time.sleep(self.delay)
        print(f"自定义线程 {self.name} 结束")

if __name__ == "__main__":
    t = MyThread("C", 1.5)
    t.start()
    t.join()