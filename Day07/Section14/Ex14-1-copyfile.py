'''
- 파일복사
    원본 -> 버퍼변수(Memory) -> 복사본
'''

buffer_size = 1024 # 1024Byte 1KB 의미
with open('hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size) # 1024Byte 단위로 읽기.
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사되었습니다')







