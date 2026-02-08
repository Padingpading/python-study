#1.定义函数，使用*args接收可变数量的位置参数
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

# 调用函数，传递多个参数
greet("Eve", "Frank", "Grace")
# 输出:
# Hello, Eve!
# Hello, Frank!
# Hello, Grace!

#2.必须位于最后一个
def args(param1, param2,*args):
    print(param1,param2,args)
    return
args(1,2,3,4,5)

