#del关键字
#我们可以使用del关键字删除对象的引用，但删除后再调用变量是会报错的，比如调用del a
# 然后再去把a打印出来，会报这样的错误：NameError: name 'a' is not defined。
a= 3
del a
a.bit_length()#NameError: name 'a' is not defined