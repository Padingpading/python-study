#1、函数也是对象
from ctypes.wintypes import tagPOINT

a1 = 100
a2= 'hello'
a3 =[10,20,30]
print(type(a1))# <class 'int'>
print(type(a2))# <class 'str'>
print(type(a3))#<class 'list'>
def welcome():
    print('欢迎来到python的世界')
print(type(welcome))#<><class 'function'>

#栈:函数名字
#堆内存:保存函数名,函数体,属性。

#2.函数可以动态太耐属性。
def welcome2():
    print('欢迎来到python的世界')
welcome2.desc="描述"
welcome2.version= 1.0;

#3、函数可以复制给变量
def welcome3():
    print('欢迎来到python的世界')
welcome3.name= 'python'
say_hello = welcome3
#执行调用
say_hello()
print(say_hello.name)

#4.可变参数vs不可变参数
a= 666
def welcome4(a):
    print(a)
    a = 888
    print(a)
welcome4(a)
print(a)

b=[10,20,30]
def welcome5(b):
    print(b)
    b.append(40)
    print(b)
welcome5(b)
print(b)

#5、数也可以作为参数
def welcome6():
    print('欢迎来 visit')
def caller(f):
    f()
caller(welcome6)

#6 函数可以作为返回值。
def website():
    def welcome():
        print('欢迎来到python的世界')
    return welcome

s = website();
s()
#直接调用。
website()();
