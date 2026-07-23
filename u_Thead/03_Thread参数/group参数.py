import threading

#  def __init__(self, group=None, target=None, name=None,  args=(), kwargs=None, *, daemon=None, context=None):
# group:
def sayHello(name,age):
    print("多线程执行")
t = threading.Thread(target=sayHello,args=("A", 2))
t.start()