# 表达式:执行后能得到值的代码,就是表达式(表达式会最终形成一个值,可以写到任何需要值的地方)

a1 = 1 + 2
a2 = 'abc' * 3  # abcabcabc

# 条件表达式:根据条件的真假,在两个结果中二选一的表达式(又称三元表达式)
age = 18
if (age >= 18):
    text = "可以投票"
    print(text)
else:
    text = "不可以投票"
    print(text)

text = "成年" if age >= 18 else "未成年"
print(text)
