#赋值运算符 =
a = 3+4
#链式赋值,引用传递
a=b=c=20
print(a,id(a))#20 1556199712
print(b,id(b))#20 1556199712
print(c,id(c))#20 1556199712

#参数赋值 += -=  *= /=  //=
a = 20
a+= 30

#系列解包赋值
a,b,c = 20,30,40
print(a)#20
print(b)#30
print(c)#40

#交换连个变量的值
g,h = 10,20
#交换
g,h = h,g
print(g)
print(h)