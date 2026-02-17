#定义一个person类(类名的通常使用:大驼峰写法)
class Person:
    #说明:当一个函数被定义在了类中时,这个函数称之为方法
    #__init__:初始化方法,主要作用:给当前创建的实例对象添加属性。
    #__init__方法收到的参数:当前正在创建的实例对象(self),其他的自定义参数。
    #当我们以后编写代码创建Person实例的时候,Python会自动调用__init__方法
    def __init__(self,name,age,gender):
        # 属性名=属性值
        self.name=name
        self.age=age
        self.gender=gender

