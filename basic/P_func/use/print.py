# 打印字符串
print("Hello, Python!")  # Hello, Python!
# 打印多个值，默认以空格分隔
print("Hello", "Python", "!")  # Hello Python !
# 自定义分隔符

# 写入到某个文件
fp=open("D:/python/python/test.txt")
print("Hello", "Python", "!", sep="-",end="ahah",file=fp)  # Hello-Python-!