'''
-튜플
    단일 변수에 여러 항목을 저장하는데 사용괸다.
    순서가 있고, 변경할 수 없는 List
    () 괄호로 작성된다.
'''
thistuple = ("피카츄", "라이츄", "꼬부기")
print(thistuple)
# 출력값 : ['피카츄', '라이츄', '꼬부기']

#튜플길이
print(len(thistuple))
print(thistuple[1])
print(thistuple[2])
print(thistuple[1:3])

#튜플값 변경 방법
thistuple = ("피카츄", "라이츄", "꼬부기")
thiscast = list(thistuple)
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)

# 튜플 압축 풀기
thistuple = ("피카츄", "라이츄", "꼬부기")
(p1, p2, p3) = thistuple
print(p1)
print(p2)
print(p3)

# 두개 튜플 조인
thistuple1 = ("피카츄", "라이츄", "꼬부기")
thistuple2 = ("버터플","야도란", "피존투", "또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)


