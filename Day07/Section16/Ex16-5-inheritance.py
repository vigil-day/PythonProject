'''

'''
class A:
    def greeting(self):
        print('안녕하세요 A입니다')

class B(A):
    def greeting(self): # 오버라이딩
        print('안녕하세요 B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요 C입니다.')

class D(B, C):
    pass    # 내부동작 필요없고 빈껍데이만 필요할때 pass

x = D()
x.greeting()
print(D.mro())










