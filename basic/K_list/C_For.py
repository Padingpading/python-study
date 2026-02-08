# # 元素在列表当中是否存在
# lst = [10, 20, 'python', 'hello']
# print(10 in lst)  # True
# print(20 in lst)  # True
# print(20 not in lst)  # False
# print(20 not in lst)  # False
#
# # 类表的遍历
# for item in lst:
#     print(item)
#
# # index遍历
# for index in range(0, len(item)):
#     print(item[index], end='\t')
#
# # enumerate遍历
# for index, value in enumerate(item):
#     print('index = %d values = %d' % (index, value))
#
# #map遍历
# # 定义一个列表
# my_list = [1, 2, 3, 4, 5]
# # 定义一个函数，用于平方
# def square(x):
#     return x ** 2
# # 使用map()函数对列表中的每个元素应用square函数
# s  = map(square, my_list);
# squared_list = list(map(square, my_list))  # map返回迭代器，需要转换为列表
# print(squared_list)

# filter遍历
my_filter_list = [1, 2, 3, 4, 5]
def gt(value,compare_value):
    return value > compare_value
filter_list = list(filter(lambda x:gt(x,3), my_filter_list))
print(filter_list)
