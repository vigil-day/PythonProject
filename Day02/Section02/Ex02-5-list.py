'''
-List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''

thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist)
print(thislist[0])

print(len(thislist)) # len 리스트의 길이를 알아내는 구문

# list 데이터 유형
list1 = ["피카츄", "라이츄", "꼬부기"]
list2 = [1, 2, 3, 5]
list3 = [True, False, False]

#다양한 유형 포함 가능
list4 = ["abc", 34, False, 40]

# 항목 접근
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1])
# 출력값 : 라이츄


# 변경
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist[1] = "잠만보"
print(thislist)
# 출력값 : ['피카츄', '잠만보', '꼬부기']

# 항목 변경 2개
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이","메타몽"]
print(thislist)
# 출력값 : ['피카츄', '울먹이', '메타몽', '파이리', '버터플', '야도란']

# 두번째 세번째 값을 하나의 값으로 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)
# 출력값 : ['피카츄', '울먹이', '파이리', '버터플', '야도란']

# 항목추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")
print(thislist)
# 출력값 : ['피카츄', '라이츄', '파이리', '꼬부기']

# 항목추가 - 인덱스번호로 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, "잠만보")
print(thislist)
# 출력값 : ['피카츄', '잠만보', '라이츄', '파이리']

# 항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.remove("라이츄")
print(thislist)
# 출력값 : ['피카츄', '파이리']

# 항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop(2)
print(thislist)
# 출력값 : ['피카츄', '라이츄']

# 마지막 값 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop()
print(thislist)
# 출력값 : ['피카츄', '라이츄']

# 목록 삭제
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear()
print(thislist)
# 출력값 : []

# 항목 확장
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터플","야도란"])
print(thislist)
# 출력값 : ['피카츄', '라이츄', '파이리', '버터플', '야도란']

# 객체 삭제
# del thislist
# print(thislist)
# 에러 뜸 (잘된거)
