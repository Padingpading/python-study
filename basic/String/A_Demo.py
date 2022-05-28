#字符串
#驻留机制:及保存一份相同且不可变字符串的方法,不同的值被存放在字符串的主流池中。
#python的驻留机制对相同的字符串值保留一份拷贝,后续创建相同的字符串时,不会开辟新空间。
#字符串的创建
a='python'
b="python"
c='''python'''
print(a,id(a))#33505056
print(b,id(b))#33505056
print(c,id(c))#33505056

#驻留机制的几种情况(交互模式下下面下起作用)
#1、字符串的长度为0或1
s1=''
s2=''
print(s1 is s2)#True

#2、符合标识符的字符串
s3 = 'abc'
s4 = 'abc'
print(id(s3))#True
print(id(s4))#True
