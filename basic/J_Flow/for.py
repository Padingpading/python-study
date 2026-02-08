#遍历 for
#语法
# for [自定义变量] in 可迭代对象
#     循环体
# 1、自定义变量可选
from traceback import format_list

# 迭代数组
fruits = ['apple','pear','watermelon']
for fruit in fruits:
    print(fruit)

#迭代字符串
for item in 'Python':
     print(item)

# range迭代
total = 0;
for  i  in range(1,100):
    total += i;
print(total)

#迭代字典
people =  {'name':'李斌','age':32}
for property,value in people.items():
    print(property)
    print(value)

# 跌打
# for循环累加和
sum = 0
for item in range(1,100):
    if item % 2==0:
       sum+=item
print("偶数和",sum)
