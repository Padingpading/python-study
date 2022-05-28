#选择
#下列的bool值都为false,反之都为true。
print(bool(False))#False
print(bool(0))#False
print(bool(1.00))#False
print(bool(None))#False
print(bool(''))#False
print(bool(""))#False
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元祖
print(bool(tuple()))#空元祖
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合

print("====================单分支=======================")
money  = 1
if money > 0:
    print("大于2")

print("====================双分支=======================")

money  = 1
if money > 2:
    print("大于0")
else:
    print("小于0")

print("====================多分支=======================")

money  = 1
if money > 2:
    print("大于2")
elif money >5:
    print("大于5")
else:
    print("小于2")

print("====================条件表达式=======================")
# 值a(true) if 条件表达式 else 值b(false)
money =  3  if 5>3  else  4
print(money)
