#浅拷贝和深拷贝
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
#变量的赋值
cpu1= CPU()
cpu2 = cpu1
print(cpu1,id(cpu1))#<__main__.CPU object at 0x0160F6B8> 23131832
print(cpu2,id(cpu2))#<__main__.CPU object at 0x0160F6B8> 23131832

disk=Disk()
computer  = Computer(cpu1,disk)
#浅拷贝
import copy
computer1=  copy.copy(computer)
print(computer,computer.cpu,computer.disk)#<__main__.Computer object at 0x01DFB4F0> <__main__.CPU object at 0x01CFF6B8> <__main__.Disk object at 0x01DFB0A0>
print(computer1,computer1.cpu,computer1.disk)#<__main__.Computer object at 0x01EE02E0> <__main__.CPU object at 0x01CFF6B8> <__main__.Disk object at 0x01DFB0A0>

#深拷贝
computerDeep = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)#<__main__.Computer object at 0x013DB4F0> <__main__.CPU object at 0x012DF6B8> <__main__.Disk object at 0x013DB0A0>
print(computerDeep,computerDeep.cpu,computerDeep.disk)#<__main__.Computer object at 0x01C80F88> <__main__.CPU object at 0x01CA4490> <__main__.Disk object at 0x01CA4B98>




