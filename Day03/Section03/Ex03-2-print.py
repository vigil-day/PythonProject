'''
- print() 함수 사용법
    sep : 출력할 value 구문 문자
    end : value 출력 후 출력할 문자 (기본 값(\n))
    file : 출력 방향 지정
'''
print("재미있는","파이썬")
print("Python", "Java", "C",sep=',')

print('안녕',end='')
print('하세요')

# 오픈 메서드를 사용하여 샘플 파일 생성후 그 파일에 프린트 출력
fos = open('sample.py', mode='wt')
print('print("Hello, World")', file=fos)
fos.close()
