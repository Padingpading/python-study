from datetime import  datetime
# 定义一个person类
from basic.P_func.use.map import result


class Person:

    plant ="地球"

    # 初始化方法
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender
    #实例方法:自定义方法
    def speak(self, msg):
        print(f'我叫{self.name} 年龄{self.age} 性别{self.gender} 我想说{msg}')

    #实例方法：自定义方法
    def run (self,distance):
        print(f'我叫{self.name} 年龄{self.age} 性别{self.gender} 跑了{distance}米')

    #定义类方法
    #作用:类方法,与类相关的逻辑,操作类级别的信息,一些工厂方法,
    # cls:类本身。
    # 1、使用classmethod装饰的方法为类方法,自定义参数。
    # 2、收到了cls参数,可以访问到任何一个类属性。
    # 功能:修改类属性
    @classmethod
    def change_plant(cls,data):
        # 没有使用self,提醒为静态方法
        cls.plant = data
        print("test1")
    # cls:类本身。
    # 功能:工厂方法
    @classmethod
    def create(cls,info_str):
        name,year,gender = info_str.split("-")
        #获取当前年份
        currentYear = datetime.now().year;
        #计算年龄
        age = currentYear-int(year);
        return cls(name,age,gender);

#类方法保存在类身上
print(Person.__dict__)#'test1': <classmethod(<function Person.test1 at 0x00000244A26C2820>)>

#类方法需要通过类调用,不需要传递cls信息。
Person.change_plant('火星')
print(Person.plant)
#实例访问
p1 = Person('张三',18,'男')
print(p1.plant)

p3=Person.create('张三-1990-男');
print(p3)

#注意点:类方法,也能通过实例访问,但是非常不推荐
p4 = p1.create('张三-1990-男');
print(p4.__dict__)