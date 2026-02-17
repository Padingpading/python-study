#定义一个person类
class Person:
    #初始化方法
    def __init__(self,name,age,gender):
        # 属性名=属性值
        self.name=name
        self.age=age
        self.gender=gender

    #自定义方法(给实例添加行为)
    #speak收到的参数是:调用speak的实例对象(self)、其他参数。
    #speak方法只有一个分,保存在Person类身上,所有Person类的实例对象,都可以调用到speak方法
    def speak(self,msg):
        print(f'我叫{self.name} 年龄{self.age} 性别{self.gender} 我想说{msg}')
# 打印类信息 'speak': <function Person.speak at 0x0000023B91B80A90>,
print(Person.__dict__)
# 创建实例对象
p1 = Person('张三',18,'男')
#验证一下 person的实例对象没有speak方法
print(p1.__dict__)

#speak方法只有一个分,保存在Person类身上,所有Person类的实例对象,都可以调用到speak方法
# 执行p1.speak方法,
#1、从实例中查找speak方法
#2、如果实例中找不到speak方法,则从类中查找speak方法
#3、如果类中找不到speak方法,则报错
p1.speak('今天天气不错')
def  speak():
    print('对象的实例方法')
p1.speak=speak
p1.speak()


