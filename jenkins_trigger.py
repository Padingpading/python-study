import threading
import time
#Thread.join() 是线程实例方法。调用该方法的线程（通常为主线程）进入阻塞状态，等待被调用的目标线程终止；目标线程运行结束后，阻塞解除，继续向下执行。
#支持设置超时时间，到达时限无论子线程是否完成，都自动解除阻塞。

# 永久等待，直到线程结束
#thread.join()
# 限时等待，单位：秒（浮点数支持小数）
#thread.join(timeout=None)

#注意点
# 谁调用 join()，谁被阻塞；t.join() → 当前执行线程等待 t 线程结束
# 线程已经执行完毕后再调用 join()，不会阻塞，直接立刻返回；
# timeout 只是等待上限，不能中断子线程执行；
# 支持重复多次调用同一个线程的 join()，不会报错；
# 底层依靠线程等待锁实现同步，用于控制多线程执行顺序。

#无限等待（最常用）
# def task():
#     time.sleep(1)
#     print("子线程执行完毕")
# if __name__ == "__main__":
#     t = threading.Thread(target=task)
#     t.start()
#     print("主线程等待子线程……")
#     t.join()   # 主线程阻塞，等待t结束
#     print("主线程继续运行")


def task_delay():
    time.sleep(5)
    print("子线程执行完毕")
t= threading.Thread(target= lambda :task_delay())
t.start()
t.join()
print("执行完毕")


#1.死锁风险：禁止在线程 A 内部调用 A 自身的 join()；禁止循环等待（A 等 B，B 等 A），程序永久卡住。
# 错误示例，死锁
def work():
    t.join()
t = threading.Thread(target=work)
t.start()