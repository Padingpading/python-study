# 四舍五入到最接近的整数  
print(round(3.14159))  # 输出: 3  

# 指定小数位数  
print(round(3.14159, 2))  # 输出: 3.14  

# 注意：当数字恰好在中间时，Python 3 的 round() 函数采用“银行家舍入”法  
print(round(2.5))  # 输出: 2  
print(round(3.5))  # 输出: 4