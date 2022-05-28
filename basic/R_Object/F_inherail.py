#继承
#格式
#class 子类名称 (父类1,父类2....)
#     pass
#1、顶层类为Object
#2、可以多继承
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

class Teacher(Person):
    def __init__(self,name,age,teacherInfoYear):
        super().__init__(name,age)
        self.teacherInfoYear = teacherInfoYear

stu = Student('张三',20,'1001')
teacher = Teacher('李四',25,12)
print(stu.name,stu.age)#张三 20
print(teacher.name,teacher.age)#李四 25


#多继承
