import threading
import time
# def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, *, daemon=None, context=None):
t = threading.Thread(target=lambda: print(f"线程里面的线程名称: {threading.current_thread().name}"))
# 获取名称
name = t.name
print(f"线程名称: {name}")
t.name = "test"
print(f"修改后的线程名称: {t.name}")
t.start()


# 获取是否守护线程
t2 = threading.Thread(target=lambda: print(f"守护线程? {threading.current_thread().daemon}"))
print(f"是否守护线程: {t2.daemon}")  # 默认 False
# 启动前可修改（启动后修改会报 RuntimeError）
t2.daemon = True
print(f"修改后是否守护线程: {t2.daemon}")
t2.start()
t2.join()

#是否存活 is_alive
t3 = threading.Thread(target=lambda: time.sleep(1))
print(f"启动前 is_alive: {t3.is_alive()}")  # False
t3.start()
print(f"运行中 is_alive: {t3.is_alive()}")  # True
t3.join()
print(f"结束后 is_alive: {t3.is_alive()}")  # False


# ident：Python 层线程标识（非零整数）
def show_ident():
    print(f"线程内部 get_ident: {threading.get_ident()}")
t4 = threading.Thread(target=show_ident, name="ident演示")
print(f"启动前 ident: {t4.ident}")  # None
t4.start()
print(f"启动后 ident: {t4.ident}")  # 非零整数，如 12345    
t4.join()
print(f"结束后 ident: {t4.ident}")  # 仍可读，值不变
# 对比：主线程的 ident
print(f"主线程 ident: {threading.current_thread().ident}")
print(f"主线程 get_ident: {threading.get_ident()}")
# 两者相等：t.ident == threading.get_ident()（在该线程自己内部时）
