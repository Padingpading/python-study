#字符串对其
#index()
s= 'hello,Hello'
#居中对齐填充到20个字符,
print(s.center(20,'*'))#****hello,Hello*****

#左对齐填充到20个字符,
print(s.ljust(20,'*'))#hello,Hello*********
print(s.ljust(20))#hello,Hello


#左对齐填充到20个字符,
print(s.rjust(20,'*'))#*********hello,Hello
print(s.rjust(20))#         hello,Hello