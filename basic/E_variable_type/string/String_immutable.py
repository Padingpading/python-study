s = 'Hello, world!'  
# 尝试修改字符串（错误示例）  
# s[0] = 'J'  # 这会引发TypeError  
  
# 正确的做法：创建一个新的字符串  
new_s = 'J' + s[1:]  
print(new_s)  # 输出: Jello, world!