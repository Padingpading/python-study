import threading

# lambda 匿名函数
t = threading.Thread(target=lambda: print(f"当前线程名称: {threading.current_thread().name}"), name="无敌线程")
t.start()
print(f"线程名称: {t.name}")
# 获取当前线程
curr_t = threading.current_thread()
curr_t.name
print(f"当前线程名称: {curr_t.name}")
