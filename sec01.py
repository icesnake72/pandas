'''
pandas & matplotlib
'''

import pandas as pd
import random

# pandas를 이용하여 1차원 배열(리스트 또는 튜플)값 읽기

# 50 ~ 100 사이의 난수를 발생하여 liNums에 10개 저장하기
liNums = [ random.randint(50, 101) for _ in range(10) ]

# # 1차원 배열 liNums의 값을 pandas의 Series객체 만들기
# # Series는 Table의 컬럼과 같다
data = pd.Series(liNums)  # , index=['유재석', '강호동', '신동엽', '김종국', '지석진', '송지효', '이광수', '김구라', '현빈', '하하']
print(data)

subject = pd.Series(['개그맨', '개그맨', '개그맨', '배우', '개그맨', '가수', '개그맨', '배우', '배우', '가수'])
grouped = data.groupby(subject)
sum_by_subject = grouped.sum()
print(sum_by_subject)

# # 데이터 생성
# data = pd.Series([1, 2, 3, 4, 5, 6])
# categories = pd.Series(['A', 'B', 'C', 'A', 'A', 'C'])

# # 카테고리에 따라 데이터를 그룹화하여 그룹별 합계 계산
# grouped = data.groupby(categories)
# sum_by_category = grouped.sum()

# print(sum_by_category)
