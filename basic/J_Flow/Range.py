#内置函数range()
#作用:生成一个整数序列
#创建range的是三种方式
#1、range(stop):创建一个[0,stop)之间的整数序列,步数为1
#2、range(start,stop):创建一个[start,stop)之间的整数序列,步数为1
#3、range(start,stop,step):创建一个[start,stop)之间的整数序列,步数为step
#返回值 一个迭代器对象。
#有点:不管range对象标识的整数序列有多长,所有range对象占用的内存空间都是相同的,
#    因为仅仅需要存储start,stop,step,只有当用到range对象的时候,词汇计算你序列中的相关元素。
#判断指定元素在序列中是否存在 in 或者 not in
#range(stop)
r=  range(10)
print(r)#range(0, 10)
print(list(r))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#range(start,stop)
r=  range(1,10)
print(r)#range(1, 10)
print(list(r))#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#range(start,stop,step)
r= range(1,10,2)
print(r)#range(1, 10, 2)
print(list(r))#[1, 3, 5, 7, 9]

print(9 in r) #true
print(10 not in r) #true