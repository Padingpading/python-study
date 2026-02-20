# 鸭子多态:如果一个东西看起来像鸭子,叫起来像鸭子,那么它就是鸭子
# 燕子类型是一种编程风格,他不检查对象的类型,只关注对象能否做某件事情
class Person:
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender
class Animal:
    def speak(self):
        print('动物叫')

class Dog:
    def speak(self):
        print('汪汪汪')
class Cat:
    def speak(self):
        print('喵喵喵')

def maje_sourd(animal):
    animal.speak()

d1 = Dog()
c1 = Cat()
a1 = Animal()

maje_sourd(d1)
maje_sourd(c1)
maje_sourd(a1)