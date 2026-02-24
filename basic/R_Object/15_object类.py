# Person类:所有的类都继承了object类,即object类是所有类顶层父类
class Person:
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender

#验证Person类是否是object类的子类
print(issubclass(Person,object))#True

print(issubclass(int,object))#True
print(issubclass(str,object))#True
print(issubclass(list,object))#True
print(issubclass(bool,object))#True
print(issubclass(tuple,object))#True

#因为 object是所有类的父亲,所以python中的所有对象,都间接是object类的实例
p1= Person ('张三',18,'男')
print(isinstance(p1,object))
print(isinstance(100,object))
print(isinstance('hello',object))
print(isinstance(True,object))
print(isinstance(None,object))
print(isinstance({'吃饭','睡觉'},object))

#所有对象都继承了object类锁提供的属性和方法,保证了每个对象有统一能力。
for attr in object.__dict__:
    print(attr)
p2= Person ('张三',18,'男')
print(p2.__dict__) #对象自己身上的东西
print(dir(p2))# 对象可以访问到的东西(自己的和继承来的)

