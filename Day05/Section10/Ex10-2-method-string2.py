'''
-
'''

# join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a1', 'b1', 'c1', 'd1', 'e1'])
print(s)

s = ' '.join(['a1', 'b1', 'c1', 'd1', 'e1'])
print(s)

# split() 메소드 - 리스트로 반환
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)

# replace()
s = 'Life is too short'
result = s.replace('short', 'log')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s ='       apple'
print(s)
result = s.lstrip() # 왼쪽 공백 제거
print(result)

s ='apple       '
print(s)
result = s.rstrip() # 오른쪽 공백 제거
print(result)

s ='      apple      '
print(s)
result = s.strip() # 양쪽 공백 제거
print(result)

# 전체 공백 제거
s = ' a p p l e '
print(s)
result = s.replace(' ', '')
print(result)

