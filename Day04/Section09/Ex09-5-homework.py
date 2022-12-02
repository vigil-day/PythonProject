'''

[회원가입]
id를 입력하세요(3글자 이상) >>>
> 3글자 이상 입력해 주세요
  id를 입력하세요(3글자 이상)

PW를 입력하세요(영문 숫자 포함 8자 이상) >>>
> 영문 숫자 포함 8자 이상 입력해 주세요

패쓰워드 확인 한번 더 입력하세요 >>>
> 일치하지 않습니다. 다시 입력하세요.

회원가입 완료

[로그인]
아이디를 입력하세요 >>>
> 아이디가 일치하지 않습니다.

아이디를 입력하세요 >>>

PW를 입력하세요 >>>
> PW가 일치하지 않습니다.

PW를 입력하세요 >>>

로그인 성공
000님 환영합니다
'''

Id = input(' 아이디를 입력하세요 >>>')
cont = 0
for ch in Id:
    if ch.isalpha():
        cont += 1
    elif ch.isnumeric():
        cont += 1

if cont >= 3:
    print('가능한 ID 입니다')
    pwd = input('비밀번호를 입력하세요 >>>')

    ch_count = 0
    num_count = 0

    for ch in pwd:
        if ch.isalpha():
            ch_count += 1
        elif ch.isnumeric():
            num_count += 1

    if ch_count >= 4 and num_count >= 4:
        ch_pwd = input('비밀번호를 한번더 입력하세요 >>>')
        while ch_pwd != pwd:
            ch_pwd = input('비밀번호가 맞지 않습니다 다시 입력하세요 >>>')
        print("회원가입 완료")

        login = input('아이디를 입력하세요 >>>')
        while login != Id:
            login = input('아이디가 맞지 않습니다 다시 입력하세요 >>>')

        password = input('비밀번호를 입력하세요 >>>')
        while password != pwd:
            password = input('아이디가 맞지 않습니다 다시 입력하세요 >>>')

        print("환영합니다 {}님".format(Id))
    else:
        print('불가능한 비밀번호 입니다')

else:
    print('id를 다시 입력하세요(3글자 이상)')


