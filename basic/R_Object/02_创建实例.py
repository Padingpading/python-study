#定义一个person类
class Person:
    #初始化方法
    def __init__(self,name,age,gender):
        # 属性名=属性值
        self.name=name
        self.age=age
        self.gender=gender
#创建Person的实例对象。
p1 = Person('dd',28,'女');
p2 = Person('ff',28,'男');

print(p1)
print(p2)
# <__main__.Person object at 0x0000023A3C0A70E0>
# <__main__.Person object at 0x0000023A3DD9C410>
# <模块.类 类型 地址>

# 通过点语法可以访问或修改实例身上的属性
print(p1.name)
print(p1.age)
print(p1.gender)
print('*' * 20)
print(p2.name)
print(p2.age)
print(p2.gender)

# 通过实例.__dict__可以查看实例上所有的属性
print(p1.__dict__)##{'name': 'dd', 'age': 28, 'gender': '女'}

#实例创建完成之后,可以通过实例.属性名=属性值去给实例追加属性
p1.address='北京'
#
print(p1.__dict__);

#通过type函数,可以查看对象是从那个类创建出来的。
print(type(p1))#<class '__main__.Person'>