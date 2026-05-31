#局部作用域
def test1(b):
    print("全局作用域a",a)
    print("局部作用域b",b)
    c = 123
    print("局部作用域c",c)
    #局部作用于inner,相对于test1函数,
    #外层函数作用域
    def inner():
        #局部作用域
        e = 400
        print('inner中的e是',e)
        # print('test1的局部作用域c是',c)
        c = 999 #c变成局部作用域
        print('inner中的c是',c)

    inner()
    print('test1的局部作用域c是',c)
test1(99)



