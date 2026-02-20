# 抽象类:是一种不能直接实例化的类,它通常作为规范,让子类继承,并实现其中的定义的抽象方法
from abc import  ABC ,abstractmethod
#MustRun一旦继承了ABC类,那么MustRun变成抽象类
class MustRun(ABC):
    # 定义抽象方法
    @abstractmethod
    def run(self):
        # 抽象方法中不会定义具体的实现
        pass
    def speak(self):
        print('人可以说话')
class Person (MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def run(self):
        print('人可以跑')
#抽象类在有抽象方法的时候,无法进行实例化.
# p1 = MustRun()
#TypeError: Can't instantiate abstract class MustRun without an implementation for abstract method 'run'



