score_dict = {
    '김자바':[90, 80],
    '이합격':[50, 77],
    '박이썬':[63, 67],
    '고길동':[82, 34]
}
"""  
아래와 같은 형태로 출력하기
1 김자바 90 80 Total: 170
2 김자바 50 77 Total: 127
3 김자바 63 67 Total: 130
4 김자바 82 34 Total: 116
"""
# 내가 함
""" for idx, (key, value) in enumerate(score_dict.items()):
    print(f'{idx + 1} {key} {value[0]} {value[1]} Total: {value[0] + value[1]}') """

# 같이 함
for idx, (key, value) in enumerate(score_dict.items()):
    total = sum(value)
    avg = total / len(value)
    info = f'{idx + 1}\t{key}\t{value[0]}  {value[1]}\tTotal: {total}\tAvg: {avg:.1f}'
    print(info)