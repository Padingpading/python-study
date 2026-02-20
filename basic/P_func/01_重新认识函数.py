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

