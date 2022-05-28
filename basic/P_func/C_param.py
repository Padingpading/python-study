#函數:返回值
#1、函数返回多个值,结果为元组
#如果函数没有返回值,return可以沈略不写。
#函数返回值是1个,直接返回类型
#函数的返回值,如果是多个,返回结果为元组

#返回空值
def funprint():
    return "ss"
print(funprint())#ss

#反会元组
def fun(num):
    odd=[]  #奇数
    even=[]  #偶数
    for i in num:
        if i%2:
           odd.append(i)
        else:
           even.append(i)
    return odd,even

lst = [10,32,6,56,98,65,98]
print(fun(lst))#([65], [10, 32, 6, 56, 98, 98])