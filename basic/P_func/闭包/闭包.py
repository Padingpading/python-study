def outer():
    num = 10
    print(id(num))  # 140711867741384
    print(hex(id(num)))  # 140711867741384
    msg = '不会被放到闭包元组'
    def inner():
        # num的生命周期和inner()函数一样
        nonlocal num
        num += 1
        print(num)

    # 返回一个函数
    print(id(inner))  # 2073081792288
    return inner

# 返回函数进行调用
f = outer()
print(id(f))  # 2073081792288
f()  # inner() 进行调用 11
f()  # inner() 进行调用 12
f()  # inner() 进行调用 13
#打印元祖
print(f.__closure__)  # (<cell at 0x000001AD6004DF60: int object at 0x00007FFA08E47528>,)
#打印某一个项
print(f.__closure__[0])  # (<cell at 0x000001AD6004DF60: int object at 0x00007FFA08E47528>,)
#打印某一项的值
#print(f.__closure__[0].content)  # (<cell at 0x000001AD6004DF60: int object at 0x00007FFA08E47528>,)
# (<cell at 0x000001AD6004DF60: int object at 0x00007FFA08E47528>,)
# 元祖结构(闭包单元,闭包单元,闭包单元)
# 元素:int类型的对象地址在 140711867741384 对应的16进制 0x00007FFA08E47528 <cell at 0x000001AD6004DF60: int object at 0x00007FFA08E47528>
#1、outer函数中,被inner所使用的变量,会被封存到闭包单元cell中。
#2、这些cell会组成一个__closure__元祖,最终放到inner函数上。

#闭包:内存函数+被内存函数所引用的外层变量
#闭包的条件
#1、函数要存在嵌套。
#2、在内存函数中,要访问外层函数的变量
#3.并且外层函数要返回内存函数,返回了内存函数,闭包才能活下来。

#注意点:
#1、在inner中未被使用的变量,不会被封存到闭包单元cell中。
#2、调用n次外层函数,就会得到n个不同的闭包,并且这个闭包互相之间不会影响。
def outout():
    num = 10
    def inner():
        nonlocal num
        num += 1
        print(num)
    return inner
f1 =outout()
f1() #11
f1() #12
f2 =outout()
f2() #11
#3.内层函数中用到的外层变量是可以变的对象,多个闭包之间依然不受影响
def outer():
    numbs = []
    def inner(value):
        nonlocal numbs
        numbs.append(value)
        print(numbs)
    return inner
f1 = outer()
f1(10)
f1(20)
f1(30)
f2 = outer()
f2(40)
f2(50)
f2(60)

