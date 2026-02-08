def args(param1, param2, param3):
    return param1 + param2


# 和顺序无关
print(args(param3=3,param1=1, param2=2))

#混合使用(所有位置传参必须位于关键字传参之前)
print(args(3,param1=1, param2=2))

# 定义