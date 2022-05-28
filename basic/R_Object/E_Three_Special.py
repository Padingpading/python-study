#面向对象的三大特性
#封装
class Student:
    #类属性
    #初始化方法,
    def __init__(self,name,age):
        #私有化name
        self.__name= name
        #私有化age
        self.__age = age
    def show(self):
        #调用私有化name
        print(self.__name+'吃饭')

stu1 = Student("张三",13)
stu1.show()#张三吃饭
#调用私有化属性方法
print(stu1._Student__age)#13


