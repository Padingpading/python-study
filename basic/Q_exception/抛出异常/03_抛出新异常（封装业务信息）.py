try:
    open("test.txt")
except FileNotFoundError:
    raise Exception("【业务异常】核心配置文件缺失，程序无法启动")