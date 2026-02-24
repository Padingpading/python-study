#概念:所谓匿名函数,就是没有名字的函数 无需使用def关键字定义
#语法:python中使用lambda关键字定义匿名函数 格式为lambda 参数:表达式
# 使用场景 当一个函数只用一个词,制作一点点事情,使用匿名函数更简介。
#注意点:
#1.只能写一行 不能写多行
#2.不能写代码块(if、for、while)
#3.冒号右边必须是表达式,且只能写一个表达式。
#4.表达式结果自动作为返回值。#使用普通函数实现计算

def add (x,y):
    return x+y
def sub(x,y):
    return x-y

def cal(fuc,x,y):
    print(fuc(x,y))

cal(add,30,20);

#匿名函数
add = lambda x,y:x+y
# 单个参数
back = lambda x:x
# 无参
empty = lambda : 1+2
print(add(1,2))
cal(lambda x,y:x+y,30,70)


