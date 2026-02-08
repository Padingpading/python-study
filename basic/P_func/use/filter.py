# 过滤出列表中的偶数
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(is_even, numbers)
# 同样地，我们需要将迭代器转换为列表来查看结果
print(list(filtered_numbers))
# 输出:
# [2, 4, 6, 8, 10]

# 过滤字典
def is_even(d):
    return d['value'] % 2 == 0
dicts = [{'value': 1}, {'value': 2}, {'value': 3}, {'value': 4}, {'value': 5}, {'value': 6}, {'value': 7}, {'value': 8}, {'value': 9}, {'value': 10}]
filtered_dicts = filter(is_even, dicts)
print(list(filtered_dicts))