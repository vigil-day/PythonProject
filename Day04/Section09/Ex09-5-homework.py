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






# 선생님 버전

Id = None
pwd = None

# 아이디 입력
while True:
    Id = input('아이디를 입력하세요(3글자 이상) >>>')

    # id_couunt = 0
    # for ch in id:
    #     id_couunt += 1
    #
    # if id_couunt > 3:
    #     break

    if len(Id) > 2:
        break
    print("> 3글자 이상 입력해 주세요")

# 패스워드 입력
while True:
    pwd = input('패쓰워드를 입력하세요(영문, 숫자 포함 8자 이상) >>>')
    isContainAlpha = False
    isContainNumeric = False
    if len(pwd) < 8:
        print('> 영문, 숫자 포함 8자 이상 입력해 주세요.')
        continue
    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True
        elif ch.isnumeric():
            isContainNumeric = True

    # 영문 포함 유효성 검사
    if not isContainAlpha:
        print('> 영문, 숫자 포함 8자 이상 입력해 주세요.')
        continue

    # 숫자 포함 유효성 검사
    if not isContainNumeric:
        print('> 영문, 숫자 포함 8자 이상 입력해 주세요.')
        continue

    #패쓰워드 한번 더 확인 유효성 검사
    pwdChk = input('패쓰워드를 한번 더 입력하세요 >>>')
    if pwd != pwdChk:
        print("> 일치하지 않습니다. 다시 입력해 주세요")
        continue

    break

print('회원가입 완료!')


# 로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 >>>')
    if Id == loginId:
        break
    print('> 아이디가 일치하지 않습니다.')

# 로그인 패쓰워드
while True:
    loginPwd = input('패쓰워드를 입력하세요 >>')
    if pwd == loginPwd:
        break
    print("패쓰워드가 일치 하지 않습니다.")

print('로그인 성공!')
print("환영합니다 {}님".format(Id))













