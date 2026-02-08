#contine:结束本次循环
sum = 0
for item in range(1,100):
    if item==50:
        sum = item
        continue
print("偶数和",sum)
#奇数和
sum_j = 0
for item in range(1,1000):
    if item%2==0:
        continue
    sum_j += item

a=  0
while a<3:
     if a==2:
       continue;
     a = a+1
print(a)

