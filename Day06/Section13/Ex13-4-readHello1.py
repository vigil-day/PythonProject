'''
    r(read mode) : 읽기 전용 모드 / 파일 없으면 에러 생성

    절대 경로 예) C:\hello.txt
    상대경로 예) ../hello.txt
               .. -> 상위폴더
               . -> 현재폴더
'''
file = open('hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()

with  open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')





