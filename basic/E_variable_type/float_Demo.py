#输出
n1 = 3.1415926
print(n1,type(n1)) #3.1415926 <class 'float'>

#浮点型的不精确输出
print(1.1+2.2)#3.3000000000000003

#精确输出
from decimal import  Decimal
print(Decimal("1.1")+Decimal("2.2"))#3.3



