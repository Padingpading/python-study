# 1.__contains__方法
my_list = ['apple', 'banana', 'cherry']
print(my_list.__contains__('apple'))

#2.表达式 in
exist  = 'cherry' in my_list;
print(exist)

#3.循环遍历判断
for i in my_list:
    if i == 'cherry':
        print('存在')
        break

