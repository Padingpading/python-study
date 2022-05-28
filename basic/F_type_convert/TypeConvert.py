
name = "黎巴嫩"
age = 20
print(type(name),type(age))
#类型之间不匹配,报错
#print(name+age)#TypeError: can only concatenate str (not "int") to str
#转换
print(name+str(age))#将age转为字符串

