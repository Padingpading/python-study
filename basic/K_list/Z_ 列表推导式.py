#[ 表达式  for 变量 in 可迭代对象  if 条件 ]
#[ item.strip()  for item in tags.split(",")  if item.strip() ]
#  └─表达式─┘    └──────遍历───────┘    └──过滤条件──┘

tags = " 动作 , 喜剧,, 爱情 "
result = []
for item in tags.split(","):
    item = item.strip()
    if item:          # 非空才要
        result.append(item)

tag_list = [ item.strip()  for item in tags.split(",")  if item.strip() ];
print(tag_list)
