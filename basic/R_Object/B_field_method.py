#类属性
class Student:
    name='lb'
    age = 13

    #初始化方法,赋值
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def eat(self):
        print("实例方法")

    @staticmethod
    def staticMethod():
        print("静态方法")

    #类方法
    @classmethod
    def classMethod(cls):
        print("类方法")

#在类之外定义的为函数,在类内定义的为方法
def drink():
    print("函数")