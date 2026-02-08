# #列表元素的获取
# #通过index获取
my_list = ['apple', 'banana', 'cherry']

#通过索引访问
print(my_list[0])
print(my_list[1])
print(my_list[2])
#没有获取到抛异常  list index out of range
# print(my_list[4])

print(my_list[-1]) #cherry
print(my_list[-2]) #banana
print(my_list[-3]) #apple

# 通过值访问,返回在列表中的位置
print(my_list.index('banana'))
#查找不到,抛出异常
print(my_list.index('not_exist_ele'))


