#文件读写

#文件打开模式
#r：读取
#w:写入
#a:追加模式
#b:二进制模式
#读取文件
file  = open('a.txt','r', encoding="utf-8")
print(file.readline())


filew  = open('b.txt','w', encoding="utf-8")
filew.write("美丽中国")
