#字符串大小写转换
#index()
s= 'hello,Hello'

#转为大写,产生新对象
upper = s.upper()#HELLO,HELLO
print(upper)

#转为小写,产生新对象
lower = s.lower()#hello,hello
print(lower)

#大写抓你小写,小写转大写
swap = s.swapcase()#HELLO,hELLO
print(swap)