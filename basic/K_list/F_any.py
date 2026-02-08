# any 是否存在任意元素
my_list = ['apple', 'banana', 'cherry']
print(any(x == 'apple' for x in my_list))
# 包含元素大于2
print(any(my_list.count('apple') > 1 for x in my_list))

