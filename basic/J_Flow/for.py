#遍历 for
#语法
# for [自定义变量] in 可跌打对象
#     循环体
# 1、自定义变量可选

#  打印字符串
for item in 'Python':
     print(item)
# range得带
for i  in range(10):
    print(i)

for _ in range(10):
    print("循环10次")

# for循环累加和
sum = 0
for item in range(1,100):
    if item % 2==0:
       sum+=item
print("偶数和",sum)