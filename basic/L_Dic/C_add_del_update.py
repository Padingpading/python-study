#字典中删除元素
#格式:del dict[key]
scores = {"张三":100,"李四":'98'}#{'张三': 100, '李四': '98'}
del scores['张三']
print(scores)#{'李四': '98'}

#清空字典的数据
#格式:dict.clear()
student = {"张三":100,"李四":'98'}#{'张三': 100, '李四': '98'}
student.clear()
print(student)#{}
#新增字典的数据
#格式:dict[key]=value
student['王五'] = 66
print(student)#{'王五': 66}
#更新字典的元素
#格式:dict[exist key] = value
student['王五'] = 77
print(student)#{'王五': 77}







