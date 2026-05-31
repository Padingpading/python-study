# nonlocal:访问外层函数的变量
#1、不能使用global,global访问的是最外层
# 局部作用域
def test():
    # 外层函数局部作用域
    c = 123
    def inner():
        # 局部作用域
        # 如何访问外层函数作用域的c变量
        nonlocal c  # 定义访问外层函数作用域的c变量
        c = 999  # 修改外层函数作用域的c变量
        print('inner中的c是', c)
    inner()
test()#调用