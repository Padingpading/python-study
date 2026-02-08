#函數:函數就是執行特定任務,完成特定功能的一段你代碼。
#函數的創建
#格式
#  def  函數 函數名([輸入參數]):
            #函数提
            #[return xxx]
#demo1
def calc(a,b):
    c= a+b
    return c
#调用方式1:实参调用
sum = calc(1,2)#
print(sum)
#调用方式2 关键字调用
sum = calc(b=1,a=2)
print(sum)#3