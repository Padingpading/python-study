#字典的遍历
scores = {"张三":100,"李四":'98'}#{'张三': 100, '李四': '98'}
for item in scores:
     # key:item
     print(item,scores[item],scores.get(item))
#张三 100 100
#李四 98 98


