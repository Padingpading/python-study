#字典
#内容:key-value
#格式: {"key":value,'key1',;value1;}
#特点
#1、key只有一个,不可以重复,value可以重复。
#2、key是无序的。
#3、key必须是不可变的对象。
#4、字典可以根据需要动态的伸缩。
#字典的創建
#花括号创建
socres = {"张三":100,"李四":'98'}#{'张三': 100, '李四': '98'}
print(socres)
print(type(socres))
#dict()创建
student  = dict(name="jacl",age=20)#{'name': 'jacl', 'age': 20}
print(student)
#空数组
d={}
print(d)#{'name': 'jacl', 'age': 20}

