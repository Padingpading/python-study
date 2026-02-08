#列表
#特点
#1、列表的顺序是有序的。
#2、索引映射唯一的数据。
#3、列表可以存储重复数据。
#4、任意类型的数据混存。
#5、根据需要动态分配和回收内存。
#一、列表的创建
#1.事例
#list = ['a','b','c',....]
#index: 0-n-1:正向  -n->1:逆向索引。
list_create = ['hello','world',98]
print(id(list_create))#31949832
print(type(list_create))#<class 'list'>
print(list_create)#['hello', 'world', 98]

#2.创建列表
#创建空列表
list_empty = []
list_obj_empty = list([])
print(list_empty)
print(list_obj_empty)
#创建有值列表

#创建方式1
list_ele  = ['hello','world',9]
# #创建方式2
list_obj_ele  = ['hello','world',9]
print(list_ele)
print(list_obj_ele)


#列表的创建

# #列表元素的获取
# #通过index获取
# a = list1[0]
# print(a)
# #通过元素获取指定位置,元素不存在，抛出异常
# print(list1.index(9))
# #从index 0--3位置查找'pad',查找不到,抛出异常
# print(list1.index("pad",0,3))
#
#

