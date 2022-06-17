#类表元素的添加
#appeng():在列表的默认添加一个元素
#extend:在列表的摸摸人至少添加一个元素
#insert:在列表表的任意位置添加一个元素
#切片:在列表的任意位置添加至少一个元素。
lst = [10,20,'python','hello']
lst.append(100)
print(lst)#[10, 20, 'python', 'hello', 100]


lst1 = ['a','b']
#添加list对象
lst1.append(lst)
print(lst1)#['a', 'b', [10, 20, 'python', 'hello', 100]]

#extend
lst2 = ['a','b']
#添加list中的元素到集合
lst2.extend(lst)
print(lst2)#['a', 'b', 10, 20, 'python', 'hello', 100]

lst3 = ['a','b']
#insert:指定位置添加元素d
lst3.insert(2,'lala')
print(lst3)#['a', 'b', 'lala']

#切片
lst4 =['a','b']
lst4[1:]='c'
print(lst4)#['a', 'c']


