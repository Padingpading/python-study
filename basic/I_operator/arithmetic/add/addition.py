print(1+1)#加法 2
a= 3
print(+a)

#一元:仅保留数值符号，不改变数值本身(表示正数)，几乎不改变结果；主要用于语法补全、代码可读性。
a = 3
c = 3.3
d = True
e =  2 + 3j
print(+a) #整型
print(+c) #浮点型
print(+d) #布尔型
print(+e) #复杂型

#二元
#1、数值类型 → 数学加法
# 1. 整数 + 整数 → 整数
print(10 + 20)       # 30
# 2. 整数 + 浮点数 → 自动提升为浮点数
print(5 + 2.5)       # 7.5
# 3. 浮点数 + 浮点数 → 浮点数
print(1.2 + 3.4)     # 4.6
# 4. 复数相加（实部+实部，虚部+虚部）
print((1+2j) + (3+4j)) # (4+6j)
# 5. 布尔值参与运算（bool 是 int 子类：True=1，False=0）
print(True + 1)      # 2
print(False + 3.5)   # 3.5
print(True + False)  # 1

#精度丢失问题
#方案 1：四舍五入（简单场景）
res = 0.1 + 0.2
print(round(res, 1))  # 0.3
#方案 2：使用 decimal 模块（金融 / 高精度计算推荐）
from decimal import Decimal
a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)  # 0.3

#重点问题 2：数值溢出
# 超大整数正常计算
print(9999999999999999999999999 + 1)
#场景二：有序序列 → 拼接操作
# 字符串 str 拼接
s1 = "Python"
s2 = " 加法运算符"
res = s1 + s2
print(res)  # Python 加法运算符

