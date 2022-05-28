#方法重写
class Aniaml(object):
    def eat(self):
        print("动物会吃")
class Dog(Aniaml):
    def eat(self):
        print("狗吃骨头")

class Cat(Aniaml):
    def eat(self):
        print("猫吃鱼")

def fun(obj):
    obj.eat()
fun(Cat())#猫吃鱼
fun(Dog())#狗吃骨头
fun(Aniaml())#动物会吃
print("================")
