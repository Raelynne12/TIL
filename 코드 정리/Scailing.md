# Scailing

> 정규화(표준화)
>
> \> 설명변수의 서로 다른 범위에 있는 것을 동일한 범주 내 비교하기 위한 작업
>
>    \- 거리 기반 모델에 필요(knn, clustering, PCA, SVM, NN ...)
>
>    \- 각 설명변수의 중요도를 정확하게 비교하기 위해
>
>    \- 이상치에 덜 민감하게 조정



1)  Standard Scailing
   - 평균을 0, 표준편차를 1로 맞추기
2)  MinMax Scailing
   - 최소값 0, 최대값 1로 맞추기
3)  Robust Scailing
   - 중앙값 0, IQR 1로 맞추기



```python
#Scailing module

from sklearn.preprocessing import StandardScalar as standard
from sklearn.preprocessing import MinMaxScaler as minmax
```

```python
#iris 데이터 로딩

from sklearn.datasets import load_iris
iris_x = load_iris()['data']
iris_y = load_iris()['target']
```

```python
# 1) standard scailing(표준화) : (x-xbar) / sigma

#직접 계산방식
(iris_x - iris_x.mean(axis = 0))/ iris_x.std(axis = 0)	#열에 있는 데이터 다 +고 /
df1 = (iris_x - iris_x.mean(axis = 0)) / iris_x.std(axis = 0)	#df1
df1.min()		#-2.43394714190809
df1.max()		#3.0907752482994253

#함수 사용
m_sc = standard()
m_sc.fit(iris_x)		#데이터를 모델에 적합하게 해주는 함수
m_sc.transform(iris_x)	#변환
```

```python
# 2) minmax scailing (x - x.min()) / (x.max() - x.min())

#직접 계산방식
df2 = (iris_x -iris_x.min(0)) / (iris_x.max(0) - iris_x.min(0))
df2.max()		#1.0
df2.min()		#0.0

#함수 사용
mm = minmax()
mm.fit(iris_x)
df2 = mm.transform(iris_x)

df2.min()		#0.0
df2.max()		#1.0
```

```python
#train/test로 분리되어진 데이터를 표준화
#70% train data / 30% test data로 나누

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)
```

```python
# 1. train_x, test_x를 동일한 기준으로 스케일링

m_sc1 = minmax()
m_sc1.fit(train_x)		#test데이터가 들어가면 안됨!

train_m_sc1 = m_sc1.transform(train_x)
test_m_sc1 = m_sc1.transform(test_x)

#훈련용 데이터에 적용
train_m_sc1.min()		#array([0., 0., 0., 0.])
train_m_sc1.max()		#array([1., 1., 1., 1.])

#테스트(검증용) 데이터에 적용
test_m_sc1.min()	#array([-0.02857143,  0.08333333,  0.01694915,  0.        ])  #0이 아님
test_m_sc1.max()	#array([0.94444444, 0.79166667, 0.96610169, 0.95833333])  
#1이 아님
```

```python
# 2. 서로 다른 기준으로 스케일링

m_sc2 = minmax()
m_sc3 = minmax()

m_sc2.fit(train_x)
m_sc3.fit(test_x)	#test data도 fit >> min을 0, max를 1

train_m_sc2 = m_sc2.transform(train_x)
test_m_sc3 = m_sc3.transform(test_x)

train_m_sc2.min()		#0.0
train_m_sc2.max()		#1.0

test_m_sc3.min()		#0.0
test_m_sc3.max()		#1.0
```

