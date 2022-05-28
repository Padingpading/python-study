#比较运算符 > <  >= <= ==
#结果:bool类型
#比较对象的值
a,b=10,20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)

#比较对象的地址值
a=10
b=10
print(a==b) #值是否相等
print(a is b)#true说明,a和b的id标识相等。

list1 = [11,22,33,44]
list2 = [11,22,33,44]
print(list1==list2) # True 比较值
print(list1 is list2) #False 比较id
print(list1 is not list2) #True

