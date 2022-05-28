#集合的增删改操作:

#=============================================集合中元素的判断#=============================================
s = {2,3,4,5,5,6,6}#{2, 3, 4, 5, 6}
print(2 in s)#True
print(100 in s)#False
print(10 not in s)#True
print(100 not in s)#True

#=============================================集合中元素添加#=============================================
s1 = {2,3,4,5,5,6,6}#{2, 3, 4, 5, 6, 80}
s1.add(80)
print(s1)

#=============================================集合中元素update#=============================================
s2 = {2,3,4,5,5,6,6}#{2, 3, 4, 5, 6, 80}
#放入列表
s2.update([100,200])
#放入集合
s2.update({400,300})
#放入字典
s2.update((700,600))
print(s1)#{2, 3, 4, 5, 6, 100, 200, 300, 80, 400, 600, 700}

#=============================================集合中元素删除#=============================================
s3 = {2,3,4,5,5,6,6}#{2, 3, 4, 5, 6, 80}
s3.remove(2)
s3.remove(200)#KeyError: 200,抛出异常
s3.discard(200)#s3.remove(200)#KeyError: 200,抛出异常
s3.pop()#删除任意元素。
s3.clear()#清空元素。
