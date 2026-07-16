import threading
import time

def task(name, sleep_time):
    """线程执行函数"""
    print(f"线程 {name} 启动，休眠{sleep_time}s")
    time.sleep(sleep_time)  # IO阻塞，释放GIL
    print(f"线程 {name} 执行完毕")

if __name__ == "__main__":
    # 创建线程对象，target=执行函数，args=元组传参
    t1 = threading.Thread(target=task, args=("A", 2))
    t2 = threading.Thread(target=task, args=("B", 1))

    t1.start()  # 启动线程，进入就绪状态
    t2.start()

    t1.join()   # 主线程阻塞，等待t1结束
    t2.join()
    print("所有子线程运行完成，主线程退出")