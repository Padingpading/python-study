#float():将其他的数据类型转换float类型
n1 = "64"
n2 = 3.144
n3 = False
#打印
print(float(n1))#64.0
print(float(n2))#3.144
print(float(n3))#0.0
#转换之后的类型
print(type(float(n1)),type(float(n2)),type(float(n3)))#<class 'float'> <class 'float'> <class 'float'>

#非数字字符串转换
n4 = "str"
print(int(n4))#ValueError: invalid literal for int() with base 10: 'str'



