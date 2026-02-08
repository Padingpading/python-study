class A:
    pass
class B:
    pass
class C(A):
    pass

if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    d = 60
    print(type(a))
    print(isinstance(a, B))
    print(isinstance(c, A))
    print("60是整形：", type(d) == int)