# 判断key是否在字典中
# 1. in
scores = {"张三": 100, "李四": '98'}  # {'张三': 100, '李四': '98'}
print(100 in scores)  # False
print('张三' in scores)  # True

# 2. 判断value相等
# 定义一个字典，包含键值对：'a' 对应 1, 'b' 对应 2, 'c' 对应 3, 'd' 对应 1
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
# 初始化一个标志变量，用于标记值 1 是否存在，初始值为 False
value_exists = False
# 遍历字典中的所有值
for item in my_dict.keys():
    # 如果当前遍历到的值等于 1
    value = my_dict.get(item);
    if (value == 1):
        value_exists = True;
    break
print(value_exists)