# 对列表中的每个数字加1
def add_one(x):
    return x + 1

numbers = [1, 2, 3, 4, 5]
result = map(add_one, numbers)
# map对象是一个迭代器，我们可以将其转换为列表来查看结果
print(list(result))
# 输出:
# [2, 3, 4, 5, 6]   