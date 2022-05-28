#循环 while
#循环分类 while  for-in
#语法结构
#while 条件表达式:
#    条件执行体(循环体)
#步骤
#1、初始化变量
#2、条件判断
#3、体检执行体
#4、改变变量
sum =0
i=1
while i<10:
    sum+=1
    i+=1
print(sum)


#1-100偶数和
a = 1
sum  = 0
while a<=100:
   if a%2:
      sum+=a

   a+=1
print(sum)

#1-100奇数和
a = 1
sum  = 0
while a<=100:
   if not a%2:
      sum+=a

   a+=1
print(sum)


