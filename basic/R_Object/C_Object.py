#类对象创建
class Student:
    #类属性
    name_pace = '类属性'
    #初始化方法,赋值
    def __init__(self,name,age):
        #实例属性
        self.name= name
        self.age = age

    #实例传入当前实例
    def eat(self):
        print("实例方法")

    @staticmethod
    def staticMethod():
        print("静态方法")

    #类方法,默认传入class
    @classmethod
    def classMethod(cls):
        print("类方法")
   #从写父类的str方法
    def __str__(self):
        print(self.name,self.age)
stu= Student("张三",32)
#查看对象的属性和方法
print(dir(stu))#
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'classMethod', 'eat', 'name', 'name_pace', 'staticMethod']
print(stu.__str__())#张三 32