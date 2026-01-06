"""  
set => 집합
- 무순서
- 데이터 중복을 허용하지 않음
- 변경 가능(mutable)
"""
set1={}   # 이건 비어있는 셋이 아니라 딕셔너리가 된다
set2 = set()    # 빈 셋을 만들고 싶다면 set()함수 활용
set3 = {1,2,3}  # 
set4 = {'H', 'e', 'l', 'l', 'o'}

print('set1:', set1, type(set1))    # set1: {} <class 'dict'>
print('set2:', set2, type(set2))    # set2: set() <class 'set'>
print('set3:', set3, type(set3))    # set3: {1, 2, 3} <class 'set'>
print('set4:', set4, type(set4))    # set4: {'l', 'e', 'H', 'o'} <class 'set'>

print(len(set4))    # 4

# set4를 for 루프 이용해서 출력해보세요
for val in set4:
    print(val, end='')  # oeHl
print()

# 데이터 추가 : add(값)
# 데이터 수정 : update(수정할값)
# 데이터 삭제 : remove(값) / discard(값)
#           remove()는 삭제할 값이 없으면 KeyError
#           discard()는 해당 값이 없더라도 오류 나지 않음
# [실습] 빈 셋을 생성 => set5
# (1) 데이터 추가하기 : 99, 88
# (2) 데이터 수정하되 [10, 100, 100] 값으로 수정하기
# (3) 데이터 삭제 : 1000 삭제
# (4) set5 출력
set5 = set()
set5.add(99)
set5.add(88)    # add()로는 1개 요소만 추가 가능
print(set5)   # {88, 99}
set5.update([10, 100, 1000])    # update()로는 여러 요소를 리스트로 추가 가능
print(set5)   # {99, 100, 1000, 10, 88}

# set5.remove(2000)   # KeyError: 2000
set5.discard(2000)   # 오류 발생 안함

set5.remove(1000)
print(set5)   # {99, 100, 10, 88}
print('---------------------------------')
# 순서를 유지해서 집합에 저장하려면?
lst = list(set5)
print(lst)   # [99, 100, 10, 88]
lst.sort()   # 원본 정렬
print(lst)   # [10, 88, 99, 100]

set6 = set(lst)
print(set6)   # set은 무순서

# 집합 연산
s1 = {1, 2, 3}
s2 = set((5, 2, 7, 1, 5))

print('s1 =', s1)   # s1 = {1, 2, 3}
print('s2 =', s2)   # s2 = {1, 2, 5, 7}
# (1) 합집합 : | 또는 union()함수
# (2) 교집합 : & 또는 intersection()
# (3) 차집합 : - 또는 difference()
# (4) 여집합 : ^ 또는 symmetric_difference()
print('------합집합 union----------------------')
print(s1 | s2)   # {1, 2, 3, 5, 7}
print(s1.union(s2))   # {1, 2, 3, 5, 7}
print('------교집합 intersection----------------------')
print(s1 & s2)   # {1, 2}
print(s1.intersection(s2))   # {1, 2}
print('------차집합 difference----------------------')
print(s1 - s2)   # {3}
print(s1.difference(s2))    # {3}
print('------여집합 symmetric_difference----------------------')
print(s1 ^ s2)   # {3, 5, 7}
print(s1.symmetric_difference(s2))   # {3, 5, 7}