#类表元素的删除
#remove(ele):
#  1、从列表中移除第一个元素,如果有重复元素只移除第一个,不存在抛异常
#  2、重复元素只删除第一个
#  3、元素不存在跑出valueError
#
#pop:
#  1、删除第一个指定索引位置的元素。
#  2、指定索引不存在抛出IndexError
#  3、不指定索引,删除列表中最后一个元素。

#切片:截取愿列表的一部分,生成一个新的列表。

#clear:清除列表中的鄋元素

#remove
lst = [10,20,'python','hello']
lst.remove(10)
print(lst)#[20, 'python', 'hello']

#pop(index)
lst1 = ['a','b']
lst1.pop(1)
print(lst1)#['a']

#切片
lst2 = ['a','b']#愿列表不变
list22= lst2[1:2]
print(list22)#['b']
#切片删除列表元素
lst2[1:2] = []
print(lst2)#['a']

#clear()
lst3 = ['a','b']
lst3.clear()
print(lst3)#[]