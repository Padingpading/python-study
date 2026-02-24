# 定义一个person类
class Person:
    # 类属性
    #1、类属性可以通过类访问,类属性是保存在类身上的。
    #2、类属性通过保存公共数据。
    max_age = 120;
    plant = '地球'

    # 初始化方法
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender
        # 年龄判断逻辑。
        if age <= Person.max_age:
            self.age= age;
        else:
            print('年龄太大了')
            self.age= Person.max_age;

#验证一下:类属性保存在类身上。
#max_age': 120, 'plant': '地球'
print(Person.__dict__)

#创建实例
p1 = Person('张三',18,'男')
p2 = Person('ff',18,'女')
#类属性可以通过实例访问,也可以通过类访问
#1、先去实例对象中查找,如果实例对象中没有,则去类中查找。
print(p1.max_age)
print(p1.plant)

#测试一下年龄超出范围.
p3 = Person('ff',200,'女')
print(p3.__dict__)

#注意点:实例.属性名=值,只会对实例对象进行属性的修改,类属性不会被修改。
p1.plant = '火星'
print(p1.plant)
print(p2.plant)
print(Person.plant)
