import threading
import time

# 1、守护线程示例
def heartbeat():
    while True:
        print("心跳上报...")
        time.sleep(1)
# if __name__ == "__main__":
#     # 设置为守护线程
#     t = threading.Thread(target=heartbeat, daemon=True)
#     t.start()
#     # 主线程运行3秒退出
#     time.sleep(3)
#     print("主线程执行结束")
# 主线程结束，心跳线程直接销毁，程序退出

# 2、daemon 特点
# 默认值：False，新建线程默认是前台非守护线程,主线程一定是非守护线程 daemon=False。
# 守护线程生命周期跟随进程内所有前台线程，不是只跟随主线程：
# 只要进程还有任意一个前台线程在运行，守护线程就继续运行；全部前台线程结束，守护线程统一销毁。
# 守护线程销毁时不会正常执行收尾逻辑，不会抛出异常、不会执行 finally，属于强制终止。
# join() 依然生效：主线程手动 t.join()，主线程会等待守护线程完成。


#守护线程可以创建新线程：新建子线程继承父线程的 daemon 属性。
# def child_work():
#     print(f"子线程 name={threading.current_thread().name}, daemon={threading.current_thread().daemon}")

# def parent_work():
#     print(f"父线程 name={threading.current_thread().name}, daemon={threading.current_thread().daemon}")
#     # 父线程是守护线程，创建子线程时不传 daemon，子线程会自动继承 True
#     child = threading.Thread(target=child_work, name="子线程")
#     child.start()
#     child.join()
# if __name__ == "__main__":
#     parent = threading.Thread(target=parent_work, name="父线程", daemon=True)
#     parent.start()
#     parent.join()
#     # 输出示例：
#     # 父线程 name=父线程, daemon=True
#     # 子线程 name=子线程, daemon=True
