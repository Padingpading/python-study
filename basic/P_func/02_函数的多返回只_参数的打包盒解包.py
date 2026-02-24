# 一、函数的多返回值
def cal (a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    # return (sum,sub,mul,div) #手动元祖
    #[sum,sub,mul,div] #手动列表
    return sum,sub,mul,div
#元组获取
result = cal(10,30);
print(result)#元组 (40, -20, 300, 0.3333333333333333)
#分别获取
r1,r2,r3,r4  = cal(20,30);

#二、参数的打包盒解包
#1.打包接收参数
# *args:打包所有的位置参数 (会形成一个元祖)
# **kwargs:打包所有的关键字参数 (会形成一个字典)
def show_info(*args,**kwargs):
    print(args)
    print(kwargs)
show_info(10,20,30,name='张三',age=18)

#三、解包传递参数
# *变量名:将元祖差竭诚一个一个独立的位置参数
# **变量名: 将字典拆解成一个一个关键字参数
def show_info2(num1,num2,num3,name,age):
    print(num1,num2,num3)
nums=(10,20,30)
names={'name':'张三','age':18}
show_info2(*nums,**names)

#三、打包传递参数和解包 一起使用
def show_info3(*args,**kwargs):
    print(args)
    print(kwargs)
nums=(10,20,30)
names={'name':'张三','age':18}
show_info3(*nums,**names)