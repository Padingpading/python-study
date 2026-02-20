#列表推导式:用一条简洁语句,从可迭代的对象中生成新列表
#备注:列表推导本质上是for+append()的一种简写方式
#语法格式:[表达式 for 变量 in 可迭代对象]
from basic.P_func.C_variavle import name

#需求 让每个列表中的元素变为原来的二倍
nums = [1,2,3,4,5]
#方式一 map方式
nums1 = list(map(lambda x:x*2,nums))
#方式二:for循环
result= []
for num in nums:
    result.append(num * 2)
#方式三:列表推导式
nums2 = [num * 2 for num in nums]

#新数组
# 加过滤条件
result_new = [i * 2  for i in range(10) if i>5]
print(result_new)

#字典推导式
names = ['张三','李四','王五']
scores = [100,98,95]
result_score = {name:score for name,score in zip(names,scores)}
result_score = {names[i]:scores[i] for i in range(len(names))}
