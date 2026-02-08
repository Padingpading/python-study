# 初始字典
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# 使用del语句删除'city'键
del my_dict['city']

print(my_dict)  # 输出: {'name': 'John', 'age': 30}

# 尝试删除不存在的键（会抛出KeyError）
# del my_dict['country']  # Uncomment to see KeyError