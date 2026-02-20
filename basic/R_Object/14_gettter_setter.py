# Person类
class Person:
    def __init__(self, name, age, id_card):
        # 实例属性 属性名=属性值
        self.name = name  # 共有属性 当前类 子类中 类外部 都可以访问
        self._age = age  # 受保护的属性 当前类 子类中 访问
        self.__id_card = id_card #私有属性 当前类 访问
    #_age的getter @property:调用的方法,但是调用者使用的时候是使用属性方式进行调用
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
         self._age = value

    @property
    def id_card(self):
        return self.__id_card
    @id_card.setter
    def id_card(self,value):
         self.__id_card = value

p1=Person('张三',18,'123456789')
print(p1.name)
# print(p1.get_age)#这样是打印的方法
p1.age=13
print(p1.age)#直接调用方法

