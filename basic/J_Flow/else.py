#else
#搭配
# if  else
# while else  循环结束之后执行else
# for else  循环结束之后执行else
i = 1
while i<5:
   print(i)
   i = i+1
#循环结束之后会调用
else:
   print("循环结束")

# 判断是否包含,不包含则执行else逻辑
fruit  =  {'苹果','香蕉','梨'}
for i in fruit:
   if i == '西瓜':
      break
else:
   print("没有西瓜")



