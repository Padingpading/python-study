import threading
import time
#概念含义
#Thread.start() 是线程实例方法，作用：启动线程活动。方法会完成底层调度，让操作系统新建内核线程，然后自动调用实例内部的 run() 方法执行目标任务。
#注意点:
#1.start() ≠ 直接执行任务函数：真正干活的是内部自动调用的 run() / target
#2.调用链：start() → OS 创建线程 → 自动调用 run() → run() 执行 target 函数
#3.状态切换：新建(NEW) → 就绪(RUNNABLE)，不代表立刻运行，需等待 CPU 调度
#4.真正实现并发：调用后主线程不会阻塞，继续向下执行
#5.每个 Thread 实例只能调用一次 start()
#6.底层封装操作系统 API（pthread_create / Windows CreateThread），由操作系统管理线程


#方式 1：基础标准用法（最常用）
# def work(name):
#     print(f"线程 {name} 开始运行")
#     time.sleep(1)
#     print(f"线程 {name} 结束运行")
# if __name__ == "__main__":
#     t1 = threading.Thread(target=work, args=("t1",))
#     t1.start()  # 启动线程，创建OS线程，执行run()
#     print("主线程继续执行")
#方式 2：继承 Thread 重写 run ()
class MyThread(threading.Thread):
    def run(self): # start()内部自动调用run
        print("自定义线程运行")
        time.sleep(1)

if __name__ == "__main__":
    t = MyThread()
    t.start()

#注意点
#1.重复执行报错
def work():
    print("执行")
t = threading.Thread(target=work)
t.start()
#t.start() # RuntimeError: threads can only be started once

