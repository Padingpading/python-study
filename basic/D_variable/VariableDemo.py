# 变量
name = "变量"
print(name)

#变量的组成
#1、标识:标识对象存储的内存地址,使用内置函数id(obj)获取
#2、类型:标识对象的数据类型,使用内置函数type(obj)来获取
#3、值:表示对象存储的具体数据,使用print(obj)可以将值打印输出
name = "变量"
print("标识",id(name))
print("类型",type(name))
print("值",name)

# 变量的多次赋值
age = "13"
age = "14"
print("年龄",age)

#  多个变量赋值
a = b = c = 1
a, b, c = 1,2,"Python"