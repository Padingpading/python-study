#int():将其他的数据类型转换int类型
n1 = "64"
n2 = 3.144
n3 = False
#打印
print(int(n1))#64
print(int(n2))#3 向下取整。
print(int(n3))#0
#转换之后的类型
print(type(int(n1)),type(int(n2)),type(int(n3)))#<class 'int'> <class 'int'> <class 'int'>

#非数字字符串转换
n4 = "str"
print(int(n4))#ValueError: invalid literal for int() with base 10: 'str'



