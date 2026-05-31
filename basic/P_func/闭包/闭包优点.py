#闭包的优点
#1.可以记住状态,不用全局变量,也不用写类,就能在多次调用之间保存数据
#2.可以做配置过的函数,先传异步分参数,把环境固定住,得到一个定制版的函数。
#3.可以实现简单的数据隐藏,外层函数不可见,只能通过内存函数方位。
#4.是装饰器等高等级用法的基础。


#文字美化操作
def beauty(char,n):
    def showMsg(msg):
        print( char*n +msg+char * n)
    return showMsg
show = beauty("*",3)
show('你好啊')
show('尚硅谷')

