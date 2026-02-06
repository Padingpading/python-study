# 整数（int）
# 浮点数（float）
# 字符串（str）
# 元组（tuple）
# 布尔值（True 和 False，实际上是int的子类）
# None（空值，也是单例对象）

# 字符串是不可变的
s = "hello"
s_new = s.replace("e", "a")  # 创建一个新的字符串对象
print(id(s) == id(s_new))  # 输出False，s和s_new的内存地址不同，因为s和s_new是不同的对象

# 元组也是不可变的
t = (1, 2, 3)
t_new = (1, 2, 3, 4)  # 创建一个新的元组对象
print(id(t) == id(t_new))  # 输出False，因为t和t_new是不同的对象

# 尝试修改元组中的元素会抛出TypeError
 #t[1] = 20  # 这是不允许的