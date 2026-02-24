# 定义一个person类
class Person:
    # 类属性
    max_age = 120;
    plant = '地球'

    # 初始化方法
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender
    #下面的speak和run方法都是实例方法,但是保存在类身上,主要让实例进行调用,都叫实例方法,
    #实例方法:自定义方法
    def speak(self, msg):
        print(f'我叫{self.name} 年龄{self.age} 性别{self.gender} 我想说{msg}')

    #实例方法：自定义方法
    def run (self,distance):
        print(f'我叫{self.name} 年龄{self.age} 性别{self.gender} 跑了{distance}米')

#创建实例
p1 = Person('张三',18,'男')
p2 = Person('李四',18,'女')
print(Person.__dict__) #有speak方法
print(p1.__dict__) #speak方法
print(p2.__dict__) #speak无方法

#通过实例调用
p1.speak('今天天气不错')
p1.run(100)
p2.speak('今天天气不错')
p2.run(100)

#通过类调用
#Person.speak('今天天气不错'); #缺少参数。
Person.speak(p1,'使用类进行调用')





