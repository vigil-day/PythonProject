'''
- 예외처리 세분화

'''
import traceback
try:
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>>'))
    print('{} / {} = {}'.format(a, b, a / b))
# except ZeroDivisionError:
#     print('0으로 나누는 것은 불가는 합니다')
# except ValueError:
#     print('정수만 입력할 수 있습니다')
except Exception as e:
    print(e)
    #예외정보 출력
    trace_back = traceback.format_exc()
    #예외상세 정보 출력
    message = str(e) + "\n" + str(trace_back)
    print(message)
    print('예외가 발생하였습니다.')









