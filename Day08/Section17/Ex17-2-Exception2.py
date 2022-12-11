'''
- 예외처리 방법
    try :
        코드 작성 영역
    except :
        예외발생시 처리구역
'''
try:
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>>'))
    print('{} / {} = {}'.format(a, b, a / b))
except:
    print('0으로 나누는 것은 불가는 합니다')