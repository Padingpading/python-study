#定义一个person类
class Person:
    #初始化方法
    def __init__(self,name,age,gender):
        #实例属性 属性名=属性值
        self.name=name
        self.age=age
        self.gender=gender

#创建实例
p1 = Person('dd',28,'女');
p2 = Person('ff',28,'男');

# 实例属性只能通过实例对象访问,不能通过类访问
print(p1.name)
print(Person.name)#AttributeError: type object 'Person' has no attribute 'name'
#每个实例对象都有自己的属性,各个实例之间互相不干扰。
print(p1.name,p1.age,p1.gender)
print(p2.name,p2.age,p2.gender)


