# 等于
print(5 == 5)  # 输出: True
print("hello" == "hello")  # 输出: True

# 不等于
print(5 != 3)  # 输出: True
print("hello" != "world")  # 输出: True

# 大于
print(5 > 3)  # 输出: True

# 小于
print(3 < 5)  # 输出: True

# 大于等于
print(5 >= 5)  # 输出: True
print(6 >= 5)  # 输出: True

# 小于等于
print(3 <= 5)  # 输出: True
print(3 <= 3)  # 输出: True

# 身份运算符
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # 输出: True，a和b指向同一个对象
print(a is c)  # 输出: False，尽管a和c内容相同，但它们不是同一个对象

# 否定身份运算符
print(a is not c)  # 输出: True