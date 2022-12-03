'''
- function
    함수(function)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합.

    def 함수이름(매개변수)
    코드 실행문
    return 반환값
'''


# welcome() 함수 정의(실행 x)
def welcome(): # 매개변수 x 리턴x
    print('Hello Python')
    print('Nice to meet you')

welcome() # 함수 호출

def introduce(name, age): # 매개변수 o 리턴x
    print('내 이름은 {}이고, 나이는 {}살 입니다'.format(name, age))

introduce('james', 25)

# 가변 매개변수 함수
def show(*args):
    print(type(args))
    for item in args:
        print(item)

show('python')
show('python', 'happy', 'birthday')

# 반환(retrun)값이 있는 함수
def address():
    srt = '우편번호 12345\n'
    srt += '서울시 영등포구 여의도동'
    return srt

result = address()
print(result)
result = address()
print(result)

# 매개변수도 o 리던 o
def plus(num1,num2):
    return num1 + num2

print(plus(1,3))
print(plus(32,20))

area = 0
def move():
    global area
    area += 1
    return area

result = move()

print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(result))
print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(result))
print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(result))
print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(result))


