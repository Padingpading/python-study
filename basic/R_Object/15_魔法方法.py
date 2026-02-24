# Person类
#魔法方法
#概念:以__xxx__命名的特殊方法(双下划线开头和结尾)
#特点:不需要手动调用,准备好这些方法,python会在特定的场景下,去自动调用
class Person:
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'我叫{self.name} 年龄{self.age} 性别{self.gender}'

    def __len__(self):
        #查看字典的长度
        return self.__dict__.__len__()

    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        # 两个字典都匹配
        return self.__dict__ and  other.__dict__

    def __getattr__(self, item):
        print(item)
        return '属性不存在'

p1 = Person('张三', 18, '男')
p2 = Person('张三', 18, '男')

print(p1.__dict__)

#调用打印方法__str__(),类似java的toString
#调用链路
#当前类
#父类
#顶层类object
print(p1)#<__main__.Person object at 0x00000174196970E0>
print(str(p1))#<__main__.Person object at 0x00000174196970E0>

#__len__ 使用len()会隐式代用__len__
#调用链路:__len__方法需要自己定义,顶级父类中没有
print(len(p1))#Expected type 'Sized', got 'Person' instead

#__lt__ 对象1<对象2 等价于  p1.__lt__(p2)
print(p1<p2) # p1.__lt__(p2)
#__gt__ 对象1<对象2 等价于  p1.__lt__(p2)
print(p1 > p2) # p1.__gt__(p2)

#__q__: 对象1 == 对象2 等价于  p1.__eq__(p2)
print("打印")
print(p1 == p2)

#__getattr__:当访问不存在的属性的时候会调用
print(p1.desc)#属性不存在
