#元组:python内置的数据结构之一,不可变序列
#不可变序列和可变序列
#不可变序列:字符串、元祖,多线程下安全。
#   没有增、删、改 操作
#可变序列:列表、字典
#   增删改操作,对象地址不发生变更。

#元组定义
#tuple=('value1','value2',....)
#1、如果元组中的对象是不可变对象,则不能引用其他对象。
#2、如果元祖中的对象是可变对象,则可变对象的引用不允许改变,单数据可以改变。

#创建方式
#1、直接小括号
t1 = ('python','word',98)
print(t1)#('python', 'word', 98)
print(type(t1))#<class 'tuple'>
#省略括号
t3 = 'python','word',98
print(t3)#('python', 'word', 98)
print(type(t3))#<class 'tuple'>
#和str的区分 ('value',) 必须加上逗号,和str区分。
t4 = ('python',)
print(t4)#('python',)
print(type(t4))#<class 'tuple'>

#2、内置函数tuple()
t2  = tuple(('python','哈哈',98))
print(t2)#('python', '哈哈', 98)
print(type(t2))#<class 'tuple'>

#空元祖
t5=()
t6 =tuple()
