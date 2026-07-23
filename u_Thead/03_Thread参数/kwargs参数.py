from threading import Thread

# 引入
def calc(a, b, desc):
    print(f"{desc}: {a + b}")
# 只能严格按 a,b,desc 顺序传，写长了极易混乱
t = Thread(target=calc, args=(10, 20, "加法运算"))
t.start()
#使用一
from threading import Thread

def print_msg(text):
    print(text)

# kwargs 字典 key 和函数形参 text 对应
t = Thread(target=print_msg, kwargs={"text": "线程测试文本"})
t.start()
t.join()