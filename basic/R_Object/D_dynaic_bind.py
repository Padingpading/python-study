#动态绑定
class Student:
    #类属性
    #初始化方法,
    def __init__(self,name,age):
        #实例属性
        self.name= name
        self.age = age
    def dat(self):
        print(self.name+'吃饭')

stu1 = Student("张三",13)
stu2 = Student("李四",13)
#动态绑定属性,
stu2.gender = '局'#当前属性只隶属于stu2对象
print(stu1.name,stu1.age)#张三 13
print(stu2.name,stu2.age,stu2.gender)#李四 13 局

#动态绑定方法
def show():
    print("绑定到stu2")
stu2.show = show()
stu2.show#绑定到stu2
