#前置知识1
#1、每次调用函数,python都会创建一个函数作用域
#2、函数执行完毕之后,函数作用域就会销毁

def  outer():
    num = 10
    num += 1
    print(num)
outer()
outer()
outer()

#前置知识二：
#1.在python中,内存函数可以方位其外层函数域中的变量
#2.访问外层函数变量无序使用nonlocal;但修改外层变量时要使用nonlocal
def outer1():
    num = 10
    def inner():
        nonlocal  num #定义当前变量是外层变量
        num = 99
        print('inner修改后',num)
    inner()
    print('outer修改后',num)
outer1()

