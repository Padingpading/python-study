# 多态:同一个方法,不同对象调用时,呈现的能力不同。
# python:标准多态,鸭子多太
class Person:
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender
class Animal:
    def speak(self):
        print('动物叫')

class Dog(Animal):
    def speak(self):
        print('汪汪汪')
class Cat(Animal):
    def speak(self):
        print('喵喵喵')

def maje_sourd(animal:Animal):
    animal.speak()

d1 = Dog()
c1 = Cat()
a1 = Animal()

maje_sourd(d1)
maje_sourd(c1)
maje_sourd(a1)