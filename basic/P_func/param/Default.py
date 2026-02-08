# 定义函数，其中一个参数有默认值
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# 调用函数，只提供必需的参数
greet("Alice")
# 输出: Hello, Alice!

# 调用函数，提供所有参数
greet("Bob", "Hi")
# 输出: Hi, Bob!

# 默认值只在函数定义时计算一次：如果默认值是一个可变对象（如列表、字典、集合等），
# 那么这个对象只会在函数定义时创建一次。这意味着如果函数修改了该对象，
# 并且后续再次调用该函数而没有为对应参数提供新的值
# ，那么修改将保留。这可能会导致意外的行为，特别是当你不希望函数之间共享状态时。
#这意味着如果函数修改了该对象，并且后续再次调用该函数而没有为对应参数提供新的值，那么修改将保留。这可能会导致意外的行为，特别是当你不希望函数之间共享状态时。#
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list
print(add_item(1))  # 输出: [1]
print(add_item(2))  # 输出: [1, 2]，而不是 [2]！

#所有默认参数都必须位于非默认参数（即必需参数）之后
def greet(name, age=0,school=""):
    return name;