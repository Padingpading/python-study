
#常用模块
#sys:python解释器和环境操作的相关的标准库
#time:和时间相关的库
#os:方法操作系统服务功能的标准库。
#calendaer:日志相关
#urllib:爬虫相关程序
#json:json序列化和反序列化
#math:数学相关
#decimal:精确的运算控制。
#loggin:日志

#第三方模块的安装
import time
import schedule

def job():
    print("定时输出")
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
