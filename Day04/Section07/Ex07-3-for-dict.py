'''
파일명 : Ex07-3-for-dict.py
for문과 dict
'''
eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}
# eng_dict_keys = eng_dict.keys()
# print(eng_dict_keys)
# for word in eng_dict_keys:
#     print('{}의 뜻: {}'.format(word, eng_dict.get(word)))

for word in eng_dict:
    print('{}의 뜻: {}'.format(word, eng_dict.get(word)))
