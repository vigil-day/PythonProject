'''
    raedline() - 파일에서 한 줄을 읽고 그 결과를 리턴
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    while True:
        str = file.readline()
        if str == '':
            break
        print(str, end='')







