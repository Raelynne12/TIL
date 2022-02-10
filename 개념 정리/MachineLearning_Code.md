## 1일차 - 자료형태의 이해



#### 범주형 자료

---

**도수분포표**

- 범주형 데이터

- 도수 : 각 범주에 속하는 관측값의 개수 value_counts()
- 상대도수  : 도수를 자료의 전체 개수로 나눈 비율 value_counts(normalize = True)
- 도수분포표 : 범주와 그 범주에 대응하는 도수, 상대도수를 나열해서 표로



**범주형 데이터**

- 수치로 측정 불가능(성별, 혈액형, 지역 등)
- 질적 자료(qualitative data)
- 분류
  - 순위형 자료(ordinal data)
    - 범주 사이 순서 의미 있음
    - 학점
    - 수치 매핑(범주를 0,1로, 세 개 이상일 때는 수치 크기 간격을 같게)
  - 명목형 자료(norminal data)
    - 범주 사이 순서 의미 없음
    - 혈액형
    - 수치 매핑, 더미기법(각 범주를 0 or 1로 변환)



**1. 불러오기**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

drink = pd.read_csv('./drink.csv') #drink라는 csv파일 데려오기
#밑에 캡쳐한 사진은 헤드만 보여준 거(상위 5개)(아래에 더 있음)
```

![image-20220211001107156](MachineLearning_Code.assets/image-20220211001107156.png)

**2. 도수 계산하기**

```python
drink['Attend'].value_counts() #도수 계산 (attend라는 열에 각 범주에 속하는 값 개수)
#0    13
#1    12
#Name: Attend, dtype: int64

drink_freq = drink['Attend'].value_counts() #이걸 drink_freq라고 새 변수에 넣기

drink[drink.Attend == 1].Name.Value_counts() #attend가 1인 것 중 name의 value_counts하기
```



#### 수치형 자료

---



**수치형 데이터**

- 수치로 측정 가능
- 양적 자료
- 키, 몸무게, 시험 점수, 나이 등
  - 이산형 자료(discrete data)
    - 셀 수 있는 관측값(뉴스 글자 수, 주문 상품 개수)
  - 연속형 자료(continuous data)
    - 연속적인 관측값(원주율, 시간)
- 많은 양 자료 > 의미있는 수치로 요약 > 대략적 분포 상태 파악 가능
- 분류
  - 평균
    - 극단적으로 큰 값이나 작은 값의 영향 많이 받음
  - 분산/표준편차
    - 퍼진 정도를 측정할 때는 이 두개로
    - 분산이 작을수록 좋음 > 평균에 몰려있으니까



**히스토그램**

- 범주형에서의 막대그래프 포지션



**1. 평균**

```python
coffee = np.array([202,177,121,148,89,121,137,158])
cf_mean = coffee.mean() # np.mean(coffee)로 해도 됨
round(cf_mean, 2) #소수점 둘째 자리까지
```



**2. 표준편차**

```python
from statistics import stdev
cf_std = stdev(coffee)
round(cf_std, 2)
```



**3. 히스토그램**

```python
flg, ax = plt.subplots()
#figure, axes객체를 포함하는 튜플을 반환
#예는 fig = figure() , ax = fig.add_subplot()한 것과 동일
plt.hist(coffee, bins = 3) #3개 계급으로 나뉜다
```

