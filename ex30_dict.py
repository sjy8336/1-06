# dict : 딕셔너리
"""  
- 순서를 기억하지 않음 (비순서)
- key값과 value값을 매핑하여 저장 (연관배열)
    참고 > js ==> json data {"id": 260106, "name": "홍길동"}
    py {key: value}
- key값의 중복은 허용하지 않음
- value값의 중복은 허용한다
- key를 이용해서 요소 추가/수정/삭제도 가능
- key를 이용해서 검색하므로 검색 속도가 빠르다

list => [], tuple => (), dict => {}. set ={}
"""
user1={
    "id": 20260106,
    "name": "김철수",
    "Python": "A",
    "Java": "B",
    "DB": "C"
}
print(user1, type(user1))   #{'id': 20260106, 'name': '김철수', 'Python': 'A', 'Java': 'B', 'DB': 'C'} <class 'dict'>
# [1] {key: value}
# [2] dict() 함수 이용하는 방법
dic1=dict({'산': 'Mountain', '바다':'Sea'})
print(dic1)

# user1에서 회원 이름을 찾아 출력하고 그 옆에 파이썬 학점도 같이 출력
print(user1['name'], '파이썬:', user1['Python'])
# 김철수 파이썬: A

# dic에서 바다에 해당하는 영어 단어를 출력
print(dic1['바다'])   # Sea

# 딕셔너리 변환하기
# 리스트 속에 튜플이나 리스트 값을 key와 value 나란히 입력하면
# dict()함수를 이용해 딕셔너리로 변환할 수 있다
lst = [ ('여름', 'Summer'), ('가을', 'Fall'), (1, 'one')]
dic2 = dict(lst)
print(dic2, type(dic2))    # {'여름': 'Summer', '가을': 'Fall', 1: 'one'} <class 'dict'>

dic3 = dict(two = 2, 셋 = 3, four = "4")
"""  
dict(key = value, key2 = value, key3 = value, ...)
주의 : dict()함수 인수에 '='연산자를 바로 사용하려면
    key가 문자열이어야 한다
"""
print(dic3)   # {'two': 2, '셋': 3, 'four': '4'}
print(dic3['셋'])
# print(dic3['one'])  # KeyError: 'one'
"""  
딕셔너리에서 key 값은
- 정수
- 실수
- 문자열 등 가능하다
- 리스트 X => mutable type 변경할 수 있는 타입은 key값으로 사용 불가
"""

# [1] 회원정보를 dict로 선언해서
# key 값에 : 이름, 아이디, 비밀번호, 성적
# value 값 : 홍길동, hone, tiger, [90, 85, 77]
# 변수명 : user2
# user2 = dict[('이름': '홍길동', '아이디': 'hong', '비밀번호':'tiger', '성적': '[90, 85, 77]')]
user2 = {
    "name": "홍길동",
    "userId":"hong",
    "passwd": "abc123",
    "score": [90, 85,77]
}
print(user2)
# R : Read = 조회
# 조회 : 변수명[키], 변수명.get(키)
print(f'''
이  름: {user2['name']}
아이디: {user2['userId']}
성  적: {user2['score']}
''')
# 변수명.get(키)
info=f'''
    Name: {user2.get('name')}
    User ID: {user2.get('userId')}
    Score: {user2.get('score')}
'''
print(info)
# 홍길동의 국어, 영어, 수학 점수를 각각 출력하세요
print(user2["score"]) # list
print("국어:", user2["score"][0]) 
print("영어:", user2["score"][1]) 
print("수학:", user2["score"][2]) 

print(user2.get('score')[0])

# print(user2['addr'])    # addr key 값은 없음   KeyError 발생
print(user2.get('addr'))    # None  key값이 없는 경우 None값을 반환. 에러나지 않음
"""  
추가 : d[키]='새로운요소'
수정 : d[키]='수정할값'
삭제 : del d[키] 또는 d.pop(키)
모두 삭제 : d.clear()
"""
# [1] user2에 우편번호와 주소를 추가하세요 (zipcode, addr)
user2['zipcode']='200'
user2['addr']='서울 동작구'
print(user2)

# [2] user2에서 비밀번호를 삭제하세요 => del
del user2['passwd']
print(user2)

# [3] user2에서 우편번호도 삭제하세요 => pop()
user2.pop('zipcode')
user2.pop('zip', None)  # zip이라는 키값이 없으면 None을 반환 / 에러나지 않음
print(user2)

# [4] user2에 저장된 항목수를 출력하세요 => len()
print('user2에 저장된 항목 수:', len(user2))

# [5] 주소를 '서울 강남구'로 수정 후 출력하세요
user2['addr']='서울 강남구'
print(user2)

"""  
dict의 모든 키 값을 추출하기 : keys() 함수
dict의 모든 벨류 값 추출하기 : values() 함수
"""
print(user2.keys())   # dict_keys(['name', 'userId', 'score', 'addr'])
print(type(user2.keys()))   # <class 'dict_keys'>

print(user2.values())   # dict_values(['홍길동', 'hong', [90, 85, 77], '서울 강남구'])
print(type(user2.values()))   # <class 'dict_values'>

# for 루프 이용해서 user2에 저장된 "키값 => 벨류값" 형태로 출력하세요
#   name => 홍길동 ...
kydict = user2.keys()

for ky in kydict:
    print(f'{ky} => {user2[ky]} or {user2.get(ky)}')

for value in user2.values():
    print(value)    # value값들만 출력. value값으로는 키 값을 알아내기 어려움.

# items() : 딕셔너리에 저장된 항목들을 반환함
print(user2.items())    # dict_items([('name', '홍길동'), ('userId', 'hong'), ('score', [90, 85, 77]), ('addr', '서울 강남구')])

# for 루프 이용해서 items() 항목들을 출력하세요
# key *** value 형태로 출력하세요
""" userItem = user2.items()
for It in userItem:
    print(f'{It[0]} *** {It[1]}') """

for k, v in user2.items():
    print(f'{k} *** {v}')

# user2의 items()이용해서 출력하되
# 앞에 1. name >>> 홍길동
#     2. userId >>> hong
# hint) enumerate() 함수 활용

for idx, (key, value) in enumerate(user2.items()):
    print(f'{idx+1} : {key} >>> {value}')