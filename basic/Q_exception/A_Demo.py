#异常
#格式

#try
#   业务逻辑
#except 异常1 as 异常对象1:
#   异常处理逻辑
#except 异常2 as 异常对象2:
#   异常处理逻辑
#except 异常3 as 异常对象3:
#   异常处理逻辑
#except 异常4 as 异常对象4:
#   异常处理逻辑
#finally:

try:
    a =int(input("输入第一个整数"))
    b =int(input("输入第二个整数"))
    result = a/b
    print("结果:",result)
except ZeroDivisionError as e:
    #小异常,打印异常
  print("出现异常了",e)
except BaseException:
  #大异常
  print("出现异常了")
finally:
  print("最后执行finally")



