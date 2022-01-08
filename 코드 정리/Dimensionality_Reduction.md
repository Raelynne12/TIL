# Dimensionality_Reduction(차원축소)

> -분석대상이 되는 여러 변수의 정보를 최대한 유지하면서
>
> '변수의 개수를 줄이는 탐색적 분석기법'
>
> -하나의 완결된 분석기법으로 사용되기보다, 다른 분석과정을 위한 전단계, 
>
> 분석 수행 후 개선 방법, 또는 효과적인 시각화 목적으로 사용
>
> -저차원으로 학습할 경우, 회귀/분류/클러스터링 등의 머신러닝 알고리즘이 더 잘 동작



```python
# 1) data loading
from sklearn.datasets import load_iris

iris_x = load_iris()['data']
iris_y = load_iris()['target']

iris_x		#변수가 4개 >> 4차원
```

```python
# 2) 2차원 축소
from sklearn.preprocessing import StandardScaler as standard
m_sc = standard()
iris_x_sc = m_sc.fit_transform(iris_x)
#PCA 적용 전 스케일링 반드시 해줘야
```

```python
# 3) 주성분 개수 설정 축소(주성분 개수 : 2개)
from sklearn.decompostion import PCA
m_pca2 = PCA(n_components = 2)		#주성분 개수 2개
iris_x_pca2 = m_pca2.fit_transform(iris_x_sc)
iris_x_pca2							#2차원으로 축소
```

```python
# 4) 유도된 인공변수로 시각화
import mglearn
#시각화 : 1, 2번째 컬럼만 뽑아
mglearn.discrete_scatter(iris_x_pca2[:,0], iris_x_pca2[:,1], y = iris_y)
#y = iris_y 안하면 다 똑같이 나옴
```

![image-20220108170855872](Dimensionality_Reduction.assets/image-20220108170855872.png)

```python
# 5) 3차원으로 축소
from sklearn.decomposition import PCA
m_pca3 = PCA(n_components = 3)
iris_x_pca3 = m_pca3.fit_transform(iris_x_sc)

from mpl_toolkits.mplot3d import Axes3D, axes3d
import matplotlib.pyplot as plt
```

```python
#도화지 그리기, 축 그리기
fig1 = plt.figure()		#도화지
ax = Axes3D(fig1)		#축

#step1. y == 0인 데이터 포인트만 시각화 << 타깃이 0,1,2로만 구서오딘
ax.scatter(iris_x_pca3[iris_y == 0,0],	  #x축 좌표
           iris_x_pca3[iris_y == 0,1],    #y축 좌표
           iris_x_pca3[iris_y == 0,2],    #z축 좌표
           c = 'blue',					  #색상
           cmap = mglearn.cm2,
           s = 60,                        #점 크기(size)
           edgecolors = 'k'   )			  #엣지컬러

#step 2. y == 1인 데이터 포인트만 시각화
ax.scatter(iris_x_pca3[iris_y == 1,0],    #x축 좌표
           iris_x_pca3[iris_y == 1,1],    #y축 좌표
           iris_x_pca3[iris_y == 1,2],    #z축 좌표
           c = 'y',
           cmap = mglearn.cm2,
           s = 60,                        #점 크기(size)
           edgecolors = 'g'               #green
           )   

#step 3. y == 2인 데이터 포인트만 시각화
ax.scatter(iris_x_pca3[iris_y == 2,0],    #x축 좌표
           iris_x_pca3[iris_y == 2,1],    #y축 좌표
           iris_x_pca3[iris_y == 2,2],    #z축 좌표
           c = 'hotpink',
           cmap = mglearn.cm2,
           s = 60,                        #점 크기(size)
           edgecolors = 'r'               #red
           )   
```

![image-20220108172243942](Dimensionality_Reduction.assets/image-20220108172243942.png)



```python
# 모델 적용(KNN - 최근접 이웃)
from sklearn.neighbors imort KNeighborsClassifier as knn

m_knn1 = knn()
m_knn2 = knn()

from sklearn.model_selection import train_test_split

train_x1, test_x1, train_y1, test_y1 = train_test_split(iris_x_pca2, iris_y, 										   random_state=0)    #이렇게 네 개로 나누겠다
train_x2, test_x2, train_y2, test_y2 = train_test_split(iris_x_pca3, iris_y, 										   random_state=0)  
#random_state=0 << 이걸 꼭 해줘야 함 계속 분석하려면  / 초기값 설정 seed값 고정함

m_knn1.fit(train_x1, train_y1)            #KNeighborsClassifier()
m_knn1.score(test_x1, test_y1)            #0.8947368421052632     #fit 한 다음 transform 안함 knn은

m_pca2.explained_variance_ratio_  #각 인공변수의 분산 설명력  #array([0.72962445, 0.22850762])  << 앞에 어레이가 압도적으로 중요한 변수
sum(m_pca2.explained_variance_ratio_)     #0.9581320720000165

m_knn2.fit(train_x2, train_y2)
m_knn2.score(test_x2, test_y2)            #0.9736842105263158

m_pca3.explained_variance_ratio_          #array([0.72962445, 0.22850762, 0.03668922])
sum(m_pca3.explained_variance_ratio_)     #0.9948212908928452
```

