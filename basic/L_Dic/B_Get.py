#字典中虎丘元素
#内容:key-value
#两种方式
#1、通过方括号
#    scores['张三']
# 如果键不存在会抛出异常
#2、get()方法
#   scores.get('张三')
# 如果键不存在返回None

#1、方括号
scores = {"张三":100,"李四":'98'}#{'张三': 100, '李四': '98'}
print(scores['张三'])#100
#print(scores["啊哈哈"])#KeyError: '啊哈哈'
#2、get()方法
print(scores.get("张三"))#100
print(scores.get("王五"))#None
print(scores.get("马奇",99))#99 值不存在,返回默认值。


#3、判断key是否存在
print("张三" in scores)#True
print("张三" not in scores)#False



