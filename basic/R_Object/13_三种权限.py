# Person类
class Person:
    def __init__(self, name, age, id_card):
        # 实例属性 属性名=属性值
        self.name = name  # 共有属性 当前类 子类中 类外部 都可以访问
        self._age = age  # 受保护的属性 当前类 子类中 访问
        self.__id_card = id_card #私有属性 当前类 访问

    def speak(self):
        print(f'我叫{self.name},年龄{self._age} 身份证{self.__id_card}')

class Student(Person):
    def hello (self):
        print(f'我是学生{self.name},年龄{self._age} 身份证{self.__id_card}')

#当前类可以覆访问所有
p = Person('张三', 18, '123456789')
p.speak()

#子类中访问不了受保护的属性
# AttributeError: 'Student' object has no attribute '_Student__id_card'. Did you mean: '_Person__id_card'?
# p = Student('张三', 18, '123456789')
# p.hello()

#类的外部。
p1 = Person('张三', 18, '123456789')
print(p1.name)
#当前类中不能访问protected,也能访问到,但是不推荐
print(p1._age)#Access to a protected member _age of a class
#类外部不能访问private,会报错
#print(p1.__id_card) #Unresolved attribute reference '__id_card' for class 'Person'
#通过 _Person 对属性重新命名的方式实现属性的私有。
print(p1.__dict__) #{'name': '张三', '_age': 18, '_Person__id_card': '123456789'}

