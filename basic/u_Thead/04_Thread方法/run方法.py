import threading
import time
#概念含义 Thread.run() 代表线程活动主体，是线程被调度后执行的逻辑入口。
#两种模式：
#使用父类默认 run()：自动执行构造参数 target 指定的函数；
#子类重写 run()：放弃 target，直接在方法内编写任务逻辑。



#方式 1：标准写法，依赖默认 run ()（传入 target）
# def task():
#     time.sleep(1)
#     print("任务执行完毕")
# if __name__ == "__main__":
#     t = threading.Thread(target=task)
#     t.start()   # 创建OS线程，新线程内部自动调用run()
#     t.join()
#二 继承 Thread，重写 run ()（不使用 target）
# class CustomThread(threading.Thread):
#     def run(self):
#         time.sleep(1)
#         print("重写run方法执行任务")
# if __name__ == "__main__":
#     t = CustomThread()
#     t.start()

#手动直接调用 run ()（仅测试，禁止用于并发）
# def task():
#     print("执行任务")
# t = threading.Thread(target=task)
# t.run()  # 在当前主线程串行执行，不存在多线程并发