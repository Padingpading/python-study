#模块导入
#格式
#import 模块名称  [as 别名]   #导入整个模块
#from 模块名称 import  属性名/方法名/类  #导入模块的属性或方法
import math
print(id(math))
print(type(math))
#Pi
print(math.pi)
#打印属性和方法
print(dir(math))
print(math.pow(2,3))#2的3次方
#向下取整和向下取整
print(math.floor(9.2))#8.0
print(math.ceil(9.5))#10

#导入自定义模块
import Z_Mondule as module
print(module.add(1,2))#3


