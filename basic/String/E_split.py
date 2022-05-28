#字符串分割
s= 'hello  Hello'

#没有指定,默认空格为分隔符
print(s.split())#['hello', 'Hello']

#按照指定分隔符分割
s1= 'hello|Hello'
print(s1.split('|'))#['hello', 'Hello']


#指定分割的次数
s1= 'hello|Hello|python'
print(s1.split('|',1))#['hello', 'Hello|python']


#从右侧开发分割 rsplit()
print(s.rsplit())
#从左侧开发分割 lsplit()
