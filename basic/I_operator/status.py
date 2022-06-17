#Python中提供了身份运算符用于「判断两个标识符是不是引用自一个对象」，is和 is not，使用示例如下：
# 普通数据类型
a = 1
b = 1
print('当前a和b引用同一个变量：%s' % (a is b))

# 复杂数据类型(数组)
a = [1]
b = [1]
print('当前a和b引用不同一个变量：%s' % (a is not b))


# 字符串
a = 'python'
b = 'python'
print('当前a和b引用同一个变量：%s' % (a is b))

#当前a和b引用同一个变量：True
#当前a和b引用不同一个变量：True
#当前a和b引用同一个变量：True