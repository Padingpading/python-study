# 一、标识符
# 1. 字母、数字和下划线：标识符可以由字母（A-Z, a-z）、数字（0-9）以及下划线（_）组成。但是，标识符不能以数字开头。
# 1  = "变量" 编译报错
# a  = 3;
# _name_  = 3; 下划线

# 2. 区分大小写：Python是大小写敏感的，因此myVar和myvar会被视为两个不同的标识符。
# myVar = '李';
# myvar = '李';

# 3. 避免保留字：不能使用Python的保留字（关键字）作为标识符。例如，if、else、for、while等都是保留字，不能用作变量名、函数名等。
# if  = '3'; 保留字报错
# 打印所有的保留字
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
#  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# import keyword
# print(keyword.kwlist)
# 4. Unicode字符：从Python 3开始，标识符中还可以使用Unicode字符（包括中文等非ASCII字符），但这通常不推荐，因为这样做可能会降低代码的可读性和可移植性。

