'''
- method 란
    특정 객체가 가지고 있는 함수를 의미한다.
    객채.메소드() 사용가능
'''

# String 객채 format 메소드
print("10자리 폭 왼 쪽 정렬 '{:<10d}".format(123))
print("10자리 폭 오른쪽 정렬'{:>10d}'".format(123))
print("10자리 폭 가운대 정렬'{:^10d}'".format(123))
print()
print("10자리 폭 왼 쪽 정렬 채움문자'{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자'{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자'{:*^10d}'".format(123))

# count() 메소드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5)
print(result)
result = s.count('best', -7)
print(result)

# find() 메소드 - 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('l')
print(result)

# 없는 값은 find -1
result = s.find('z')
if result == -1:
    print("존재하지 않는 문자입니다")
print(result)

s = 'best of best'
result = s.find('best', 5)
print(result)
result = s.find('best', -7)
print(result)

# index() == find() 하지만 문자열이 존재하지 않으면 index에선 에러발생
s = 'apple'
result = s.index('p')
print(result)

# result = s.index('z')
# print(result)



