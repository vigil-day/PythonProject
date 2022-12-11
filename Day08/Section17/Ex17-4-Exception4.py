'''
- finally
    try 절에서 예외 발생여부 관계없이 항상 실행
- else
    try 절에서 except 절이 실행되지 않으면  실행
'''

import traceback
try:
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>>'))
    print('{} / {} = {}'.format(a, b, a / b))

except ZeroDivisionError:
    print('0으로 나누는 것은 불가는 합니다')

except ValueError:
    print('정수만 입력할 수 있습니다')

except Exception as e:
    print(e)
    #예외정보 출력
    trace_back = traceback.format_exc()
    #예외상세 정보 출력
    message = str(e) + "\n" + str(trace_back)
    print(message)
    print('예외가 발생하였습니다.')
else:
    print('예외가 발생하지 않을때 실행')
finally:
    print('반드시 출력해 주세요!!!')
