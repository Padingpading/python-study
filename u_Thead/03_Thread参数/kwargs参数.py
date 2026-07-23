from threading import Thread

# 引入
def calc(a, b, desc):
    print(f"{desc}: {a + b}")
# 只能严格按 a,b,desc 顺序传，写长了极易混乱
t = Thread(target=calc, args=(10, 20, "加法运算"))
t.start()
#场景 1：基础单关键字传参
def print_msg(text):
    print(text)
# kwargs 字典 key 和函数形参 text 对应
t = Thread(target=print_msg, kwargs={"text": "线程测试文本"})
t.start()
t.join()

#场景2:混合 args + kwargs（位置 + 关键字混用）
# name、age 走位置传参，city 使用关键字
t = Thread(
    target=lambda name, age, city: print(f"姓名:{name},年龄:{age},城市:{city}"),
    args=("张三", 22),
    kwargs={"city": "上海"},
)
t.start()
t.join()

#场景3:函数存在默认参数，仅传递部分参数
def log(level="INFO", msg="空消息"):
    print(f"[{level}] {msg}")
# 只覆盖 msg，level 使用函数默认值
t1 = Thread(target=log, kwargs={"msg": "用户登录成功"})
# 覆盖两个参数
t2 = Thread(target=log, kwargs={"level": "ERROR", "msg": "接口请求失败"})
t1.start()
t2.start()
t1.join()
t2.join()

#场景4解包外部字典批量传参（业务高频
def upload(file, path, timeout=30):
    print(f"上传{file}至{path},超时{timeout}s")
param_dict = {
    "file": "data.csv",
    "path": "/data/upload",
    "timeout": 60
}
# 直接传入完整参数字典
t = Thread(target=upload, kwargs=param_dict)
t.start()
t.join()
#注意点:
# 1.精准绑定：通过参数名匹配，不会出现 args 顺序错位 bug
# 2.顺序无关：字典键值对无序，不用匹配函数形参书写顺序
# 3.支持默认参数：字典内可省略带默认值的形参，函数自动填充默认值
# 4.兼容混合传参：可与 args 位置参数同时使用，分工清晰
# 5.多类型兼容：字典 value 支持数字、字符串、列表、自定义对象、锁、队列等任意 Python 对象
# 6.线程隔离传参：每个线程的 kwargs 字典相互独立，互不污染



#1.类型强制校验kwargs 只能传 dict，传列表 / 元组会直接抛 TypeError
# 错误写法
# t = Thread(target=upload, kwargs=[10, 20, "加法运算"]) 
# t.start()
# t.join()
#TypeError: __main__.upload() argument after ** must be a mapping, not list


#2禁止 args、kwargs 重复传递同一参数
#同一个形参不能既在 args 传、又在 kwargs 传，触发 TypeError: got multiple values for argument
# 错误写法：city 既在 args 位置传，又在 kwargs 里传
# t = Thread(target=lambda name, age, city: print(f"姓名:{name},年龄:{age},城市:{city}"), 
# args=("张三", 22, "北京"), kwargs={"city": "上海"})
# t.start()
# t.join()
#TypeError: <lambda>() got multiple values for argument 'city'

#3.key 名称必须和函数形参完全一致大小写敏感、不能少字符，不存在的参数名会报 TypeError: unexpected keyword argument
# 错误：键名写错 Name≠name
st = Thread(target= lambda name: print(name),kwargs={"name": "李四","Name":"哈哈"})
st.start()
#TypeError: <lambda>() got an unexpected keyword argument 'Name'. Did you mean 'name'?
#4.可变对象共享风险（线程安全重点）
#若 kwargs 内 value 是列表、字典等可变对象，多个线程共用同一个对象会产生数据竞争，需加锁保护
# data = []
# def add_item(item_list, num):
#     item_list.append(num)
# # 两个线程共用同一个列表，会出现数据错乱
# t1 = Thread(target=add_item, kwargs={"item_list": data, "num": 1})
# t2 = Thread(target=add_item, kwargs={"item_list": data, "num": 2})


#5、区分 Thread 自身参数与 target kwargs 
# Thread 的 name、daemon、group 属于线程构造参数，不能放进 kwargs 字典，kwargs 仅用于目标函数传参
# 错误：daemon 是 Thread 参数，不是目标函数参数
# t1 = Thread(target=lambda daemon: print(daemon), kwargs={"daemon": True})
# t1.start()

#6.无关键字参数的函数，传 kwargs 空字典不报错python
# def test(a): pass
# Thread(target=test, args=(1,), kwargs={"b":"123"})  # 合法，无任何问题

st = Thread(target= lambda name: print(name),kwargs={"name": "李四","Name":"哈哈"})
st.start()