# 字典 报错
# {"name":"Tom"} + {"age":18}

# 集合 报错
# {1,2} + {3,4}

# bytes 拼接仅同类型可用
b1 = b"abc"
b2 = b"123"
print(b1 + b2)  # b'abc123'

# 其他方法 
#1、字典拼接
# 字典合并：Python3.5+ 使用 ** / |
d1 = {"a":1}
d2 = {"b":2}
new_d = {**d1, **d2}
print(new_d)  # {'a': 1, 'b': 2}


# 集合合并：使用 union() 或 |
s1 = {1,2}
s2 = {3,4}
print(s1 | s2)        # {1,2,3,4}
print(s1.union(s2))

