#列表
#列表的创建
#list = ['a','b','c',....]
#index: 0-n-1:正向  -n->1:逆向索引。
#特点
#1、列表的顺序是有序的。
#2、索引映射唯一的数据。
#3、列表可以存储重复数据。
#4、任意类型的数据混存。
#5、根据需要动态分配和回收内存。
list = ['hello','world',98]
print(id(list))#31949832
print(type(list))#<class 'list'>
print(list)#['hello', 'world', 98]

#列表的创建
#创建方式1
list1  = ['hello','world',9]
#创建方式2
#list2 = list(['hello','word',98])

#列表元素的获取
#通过index获取
a = list1[0]
print(a)
#通过元素获取指定位置,元素不存在，抛出异常
print(list1.index(9))
#从index 0--3位置查找'pad',查找不到,抛出异常
print(list1.index("pad",0,3))



