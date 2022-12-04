'''
    file 객체 read() -> 전체 읽어오기
         객체 read(인수) -> 인수값 만큼 읽어 오기
'''

file = open('hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5)
    if not str: # 읽을 값이 없으면 True
        break
    print(str, end='')

file.close()















