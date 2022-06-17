#元素在列表当中是否存在
lst = [10,20,'python','hello']
print(10 in lst)#True
print(20 in lst)#True
print(20 not in lst)#False
print(20 not in  lst)#False


#类表的遍历
for item in lst:
    print(item)

for index in range(0, len(item)):
    print(item[index], end='\t')

for index, value in enumerate(item):
    print('index = %d values = %d' % (index, value))