'''
- Dictionary
    key:value로 이루어져 쌍으로 데이터 값을 저장하는데 사용
'''

# Dictionary 선언
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2002
}
print(thisdict)

'''
키 이름을 사용하여 참조할 수 있다.
'''

# 값 가져오기
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2002
}
print(thisdict["brand"])
print(thisdict.get("model"))


# 키 목록 가져오기
print(thisdict.keys())






