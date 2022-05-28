#函數变量;

#全局变量

#局部变量:在函数体内定义的变量

def funprint(a,b):
    c=a+b#局部变量
    print(c)

name ='方法调用全局变量'
def fun2():
    print(name)#方法调用全局变量
fun2()

#在方法内部创建全局变量
def fun3():
    global age
    age = 30
    print(age)#30
fun3()
print(age)#30

