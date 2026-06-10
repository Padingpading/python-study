#Python提供了成员运算符，用于「判断指定的序列中是否有某个特定的值」，in 和 not in，
#比如判断列表中是否有某个特定的值的代码示例如下：
people_list = ['小明', '小红', '小白', '小猪']
if '小猪' in people_list:
    print("小猪在列表里")
if '大猪' not in people_list:
    print("大猪不在列表里")