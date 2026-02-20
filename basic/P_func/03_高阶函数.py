#高阶函数:当一个函数的参数是函数或者返回只是函数的时候,那么这个函数就是一个高阶函数。
#作用:
#1.代码复用性高,可以吧行为独立出去,传入不同函数实现不同逻辑。
#2.能函数更灵活,更通用。
#3.告诫函数式:装饰器、闭包的基础。

def info(msg):
    return '[提示]:'+msg
def warning(msg):
    return '[警告]:'+msg
def error(msg):
    return '[错误]:'+msg

def log(func,text):
    print(func(text))

log(info,'文件保存成功!')
log(warning,'磁盘空间不足!')
log(error,'该用户不存在!')


