#方法重写


class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age;

#创建C类对象
x=  C('李斌',20)
# ===============================================属性====================================
#__dict__:查看字典信息
#查看对象的属性字典
print(x.__dict__)#{'name': '李斌', 'age': 20}
#查看类的字典信息
print(C.__dict__)#{'__module__': '__main__', '__init__': <function C.__init__ at 0x014426E8>, '__doc__': None}

#查看对象的类型 __class__
print(x.__class__)#<class '__main__.C'>

#查看父类的类型,返回元组
print(C.__base__)#<class '__main__.A'>
print(C.__bases__)#(<class '__main__.A'>, <class '__main__.B'>)
#查看类层次结构
print(C.__mro__)#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
#查看子类列表
print(A.__subclasses__())#[<class '__main__.C'>]

# ===============================================方法====================================

#add
a = 1
b= 3
#下列等价
c = a+b
d = a.__add__(b)

class Student:
    def __init__(self,name):
        self.name = name
    #重写add
    def __add__(self, other):
        return self.name+other.name
stu1 = Student('张三')
stu2 = Student('李四')
s = stu1+stu2
print(s)#张三李四

