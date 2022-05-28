#init 和new

class Persion(object):
    def __init__(self,name,age):
        print("__init__被调用了,self的id置位:0{}".format(id(self)))
        self.name =name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__被执行调用了,clas的id值为{0}".format(id(cls)))
        #创建实例对象
        obj = super().__new__(cls)
        print("创建对象的id值为{0}".format(id(cls)))
        return obj


print("object这个类对象的id值为{0}".format(id(object)))
print("Persion这个类对象的id值为{0}".format(id(Persion)))

#创建person的实例对象
p1 = Persion("张三",20)
print("p1这个Person类的实例对象的id{0}".format(id(p1)))
