from datetime import  datetime
# 定义一个person类
from basic.P_func.use.map import result

class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        # 实例属性 属性名=属性值
        self.name = name
        self.age = age
        self.gender = gender

    #静态方法
    #1、@staticmethod装饰过的方法为静态方法,静态方法保存在类身上。
    #2、静态方法只是单纯定义在类中,他不会收到self,cls参数,收到的参数全部都是自定义参数。
    #3、由于静态方法中不收到self,cls参数,所以其内部不会访问任何类和实例相关的内容。
    #4、静态方法通常用户定义与类相关的工具。
    @staticmethod
    def is_adult(year):
        currentYear = datetime.now().year;
        age = currentYear -year;
        if(age>18):
            return True;
        return False;
    @staticmethod
    def mark_idcard(idcard):
        return idcard[:6] + "********" + idcard[-4:]
# 验证一下静态方法在类的身上
#'is_adult': <staticmethod(<function Person.is_adult at 0x000001E2A12E2560>)>
print(Person.__dict__)

#静态方法需要通过类调用
print(Person.is_adult(1990))
print(Person.is_adult(2010))
id_mark = Person.mark_idcard("142322199401163037")
print(id_mark)

#注意点,通过实例也能调用静态方法。
