# 异常继承体系
# BaseException  # 所有异常的顶级父类
#  └── Exception  # 普通业务异常父类（我们99%捕获的都是这个）
#       ├── ValueError
#       ├── TypeError
#       ├── IndexError
#       ├── KeyError
#       └── ...
#  └── 系统级异常（不建议捕获）
#       ├── KeyboardInterrupt
#       ├── SystemExit
#       └── GeneratorExit

# 1. 高频常用异常（90%场景都会遇到）
# - ZeroDivisionError：除数为0
# - ValueError：数值类型错误（字符串转数字失败、参数不合法）
# - TypeError：类型错误（字符串+数字、参数类型不对）
# - IndexError：列表/字符串索引越界
# - KeyError：字典不存在对应的key
# - FileNotFoundError：文件不存在
# - PermissionError：权限不足，无法读写文件
# - AttributeError：对象无该属性/方法
# - NameError：变量未定义
# 2. 中频进阶异常
# - AssertionError：断言失败（assert 判断不成立）
# - EOFError：读取数据到末尾，无输入
# - KeyboardInterrupt：手动终止程序（Ctrl+C）
# - MemoryError：内存溢出
# - RecursionError：递归深度超限（死递归）
# - TimeoutError：请求/连接超时
# - ConnectionError：网络连接异常