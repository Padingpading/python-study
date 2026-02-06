#定义数组
s = 'Hello, world!'
#获取数组长度
length = len(s)
print(f"字符串的长度是{length}")
# 输出第一个
print(s[0])  # 输出: H
# 输出的第二个
print(s[1])  # 输出: e
# 输出的第三个
print(s[3])  # 输出: l
# 最后一个
print(s[length-1])
# 数组越界 异常
#print(s[length]) #IndexError: string index out of range
#最后向前遍历
print(s[-1]) # 输出: !（负索引从字符串末尾开始）