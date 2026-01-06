# 컴프리헨션 - 반복문 축약
# 파이썬에서는 4가지 종류의 축약을 지원한다.
# list / set / dict / generator

# list에 적용하는 축약
# (1) 변수 = [실행문 for 변수 in 열거형객체]
# (2) 변수 = [실행문 for 변수 in 열거형객체 if 조건식]
# (3) 변수 = [실행문1 if 조건 else 실행문2
#               for 변수 in 열거형 객체]

nums = [i for i in range(1, 11)]    # 축약식
print(nums)

nums2 = list(range(1, 11))
print(nums2)

# (1) 1 ~ 10 사이의 값의 5배 값을 갖는 리스트를 lst1에 할당 후 출력
lst1 = [a * 5 for a in range(1, 11)]
print(lst1)

# (2) 0 ~ 20 사이의 짝수를 리스트로 생성하는 축약문 작성 후 출력
lst2 = [b for b in range(0, 21) if b % 2 == 0]
print(lst2)
lst3 = [i for i in range(0, 21, 2)]
print(lst3)

# (3) 1 ~ 10 까지의 값의 제곱 값을 리스트로 생성하는 축약문 작성 후 출력
lst4 = [c ** 2 for c in range(1, 11)]
print(lst4)

# (4) 1 ~ 20 까지 수 중 짝수가 위치한 곳에는 'even'을 홀수가 위치한 곳에는 'odd'를 
# 담는 lst5 생성 후 출력 if ~ else 사용
lst5 = ['even' if i % 2 == 0 else 'odd' for i in range(1, 21)]
print(lst5)

# 딕셔너리 축약문 ==> { } 사용
# 변수 = {표현식 for key, value in zip(열거형객체1, 열거형객체2)}

names = ['김영철', '최미나', '서희영']
grades = ['A', 'C', 'B']

# 축약문 이용해서 names와 grades를 키와 값으로 매핑한 딕셔너리로 만드세요
# 변수명: dct
dct = {k:v for k, v in zip(names, grades)}
print(dct)
print(zip(names, grades))   # <zip object at 0x000001D03625B980>

students = ['철수', '영희', '길동', '민형']
scores = [50, 80, 95, 60]
# 60점 이상이면 합격 그렇지 않으면 불합격
# 철수: 불합격
# 영희: 합격 ... -> dict 에 담아 출력하세요
# 축약식을 사용하세요

# 내가 함
dict1 = {f'{k}: 합격' if v >= 60 else f'{k}: 불합격' for k, v in zip(students, scores)}
print(dict1)

# 다른 방식
dct2 = {std: '합격' if score >= 60 else '불합격' for std, score in zip(students, scores)}
print(dct2)

jumsu = (('김성한', 88, 85, 99),)
# jumsu 에서 이름과 국어 점수만 추출하세요
name, kor, eng, math = zip(*jumsu)   # *jumsu : tuple unpacking
print(name[0], kor[0])      # **dict : dict unpacking

# dict 축약문 : {key:value for 변수 in 열거형 긱}
# set에 축약문 사용 : {value for 변수 in 열거형 객체}

nums = [1, 2, 2, 3, 4, 5, 1, 1]
# nums 에서 중복되지 않는 값들만 추출하여 set 객체로 출력하세요. 축약문 사용
st = {x ** 3 for x in nums}
print(st)   # {64, 1, 8, 27, 125}
st2 = set(nums)
print(st2)

# 중첩 for문 축약문
# [표현식 for a in A for b in B]
A = [1,2,3]
B = [4,5,6]
# A * B 의 결과값을 result 변수에 담되 list 형태로
# 축약문 사용해서
# result = [4, 5, 6, 8, 10, 12, 12, 15, 18]
result = [a * b for a in A for b in B]
print(result)   # [4, 5, 6, 8, 10, 12, 12, 15, 18]