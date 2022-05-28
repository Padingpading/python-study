#集合的关系

#集合是相等
s = {2,3,4,5}
s1 = {5,4,3,2}
print(s==s1)#True 比较的是指是否相等。
print(s!=s1)#False

#集合是是子集和超集
s1 = {5,4,3,2}
s2 = {5,4,3,2,3}
print(s1.issubset(s2))#True s1是不是s2的自己。
print(s2.issuperset(s1))#True s1是不是s2的自己。


