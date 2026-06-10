#1.字符串拼接
s1 = "Python"
s2 = " 加法运算符"
res = s1 + s2
print(res)  # Python 加法运算符

#1.1禁止字符串 + 数字，类型不匹配直接报错
#print("年龄：" + 18)  # 年龄：18
# 报错：TypeError: can only concatenate str (not "int") to str
# "年龄：" + 18
print("年龄：" + str(18))  # 年龄：18

#1.2字符串是不可变对象：s1 + s2 会生成全新字符串，原字符串不变。
s3 = "1"+"2"
print(s3)

#1.3大量循环拼接字符串：禁止反复使用 +，性能极差。
s = ""
for i in range(1000):
    s += str(i)
#高效写法（推荐 str.join()）
lst = [str(i) for i in range(1000)]
s = "".join(lst)
print(s)
ssss = range(1000)

#1.4 只能 列表 + 列表，不能和单个元素、字符串、元组相加：

