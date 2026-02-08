scores = {"张三":100,"李四":'98'}#{'张三': 100, '李四': '98'}
#获取字典中所有的key
keys = scores.keys();
print(keys)#dict_keys(['张三', '李四'])
print(type(keys))#<class 'dict_keys'>
#所有key转为list
print(list(keys))#['张三', '李四']

#获取所有的value
values =  scores.values();
print(values)#dict_values([100, '98'])
print(type(values))#<class 'dict_values'>
print(list(values))#[100, '98']

#获取所有的键值对
items =  scores.items();
print(items)#dict_items([('张三', 100), ('李四', '98')])
print(type(items))#<class 'dict_items'>
print(list(items))#[('张三', 100), ('李四', '98')]




