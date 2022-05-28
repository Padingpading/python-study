#集合:

#集合的创建
#格式:set={'value1','value2',.....}
#特点
#1、集合中的元素是允许重复的。
#1、{}创建
s1 = {2,3,4,5,5,6,6}#{2, 3, 4, 5, 6}
print(s1)
#2、内置函数set()
s2 = set(range(6))
print(s2)

#列表转集合
s3 = set([1,2,3,4,5,6])
print(s3)#{1, 2, 3, 4, 5, 6}

#元组转集合
s4 = set((1,2,3,4,5,65))
print(s4)#{1, 2, 3, 4, 5, 65}


#字符串转集合
s5 = set('python')
print(s5)#{'y', 'h', 'o', 'n', 'p', 't'}

#定义空集合
s6 = set();
print(s6)#set()