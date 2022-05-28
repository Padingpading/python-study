#
#引入自定义模块
import  Z_Mondule as module

#只有是主程序的时候才会调用,当前模块,其他模块不会执行。
if  __name__ =='__main__':
    print(add(10,20))