#方法重写
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no

    #重写父类中的方法
    def info(self):
        #调用父类中的方法
        super().info()
        #自己方法中的内容
        print(self.stu_no)

stu = Student('张三',20,'1001')
stu.info()
#张三 20
#1001
