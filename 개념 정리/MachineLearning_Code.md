## 1일차 - 자료형태의 이해



#### 범주형 자료

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



---



## 2일차 - 데이터 전처리

> 실제로 데이터를 전처리 해보기



**전처리의 역할**

1. 머신러닝의 입력 형태로 데이터 변환
   - 대부분은 숫자 데이터 입력받음, but 실제 데이터는 다양해서 수치형 자료로 바꿔줘야
2. 결측치, 이상치 처리해서 데이터 정제
3. 학습용, 평가용으로 데이터 분리



**데이터 정제 및 분리**

- 결측값 처리
- 이상치 처리
  - 모델 성능 저하될 수 있음
  - 통계지표(카이제곱 검정, IQR 지표 등) 사용해서 판단
  - 데이터 분포보고 직접 판단
- 지도학습 데이터 분리
  - feature/label : 예측하기 위한 입력값 / 예측할 대상이 되는 데이터



**범주형 데이터**

**1. 데이터 불러오기**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./titanic.csv')
```

![image-20220211004835184](MachineLearning_Code.assets/image-20220211004835184.png)



**2. replace하기(문자를 숫자로)**

```python
df = df.relace({'male':0, 'female':1}) #딕셔너리 형태로 replace
#남자는 0, 여자는 1로 바꿈
```



**3. dummy 방식(명목형 자료 변환)**

```python
pd.get_dummies(df.Embarked) #get_dummies 사용해서 변환
#embarked열 값들이 c,q,s인데 이걸 0, 1로 변환
```

![image-20220211005245498](MachineLearning_Code.assets/image-20220211005245498.png)



**수치형 데이터**

**1. 정규화 함수 구현(minmax scaling)**

```python
def normal(data):
    maxx = max(data)
    minn = min(data)
    data = (data-minn)/(maxx-minn)
    return data
print(df.Fare.head())
df.Fare = normal(df.Fare)
df.Fare.head()
```

![image-20220211005550352](MachineLearning_Code.assets/image-20220211005550352.png)



**2. 표준화 함수 구현(standardzation)**

```python
#x-(x.mean)/x.std << 표준화
def standard(data):
    data = (data - data.mean()) / data.std()
    return data
print(df.Fare.head())
df.Fare = standard(df.Fare)
df.Fare.head()
```

![image-20220211005732735](MachineLearning_Code.assets/image-20220211005732735.png)

**3. 결측치 처리**

```python
df.info()
##   Column       Non-Null Count  Dtype  
#---  ------       --------------  -----  
# 0   PassengerId  891 non-null    int64  
# 1   Survived     891 non-null    int64  
# 2   Pclass       891 non-null    int64  
# 3   Name         891 non-null    object 
# 4   Sex          891 non-null    object 
# 5   Age          714 non-null    float64
# 6   SibSp        891 non-null    int64  
# 7   Parch        891 non-null    int64  
# 8   Ticket       891 non-null    object 
# 9   Fare         891 non-null    float64
# 10  Cabin        204 non-null    object 
# 11  Embarked     889 non-null    object 

#cabin은 null이 너무 많아서 지워버리고
#embarked는 null값 두 개 처리하고(대체)
#age는 좀 봐야겠네
#라고 판단
```

```python
#1. cabin  변수 제거
df = df.drop(columns = ['Cabin'])

#2. 결측값 포함되어있는 샘플 제거
df = df.dropna()  #왜 대체안하고 그냥 drop했는지는 기억이 안남
```



**4. 이상치 처리**

```python
df.boxplot() #age, fare가 이상치가 엄청 많네
```

![image-20220211010250392](MachineLearning_Code.assets/image-20220211010250392.png)

```python
#age값 - age내림값(기준) > 0보다 크면 소수점 갖는 데이터로 분류

df.Age
np.floor(df.Age) #내림값

outlier = df[df.Age - np.floor(df.Age) > 0] #0보다 큰 값들을 나오게 함(이상치들)
#왜냐하면 나이에는 실수형이 없으니까
df_final = df[df.Age - np.floor(df.Age) = 0] #정상값(소수점 없는)

len(outlier) #25개
```



**5. 모델링**

```python
#1. 데이터 분리
from sklearn.model_selection import train_test_split

#feature data, label data(지도학습)
X = df_final.drop(columns = ['Survived']) #아까 그 정상값들 중에 survived drop
y = df_final['Survived'] #정상값들의 survived 열

print('X의 데이터 개수 : %d'%(len(X)))
print('y의 데이터 개수 : %d'%(len(y)))

#출력결과
#X의 데이터 개수 : 687
#y의 데이터 개수 : 687

#train data, test data로 분리
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 42) #42인 이유 : 노가다 해보니 얘가 제일 값이 잘 나오더라

print('학습한 데이터 개수 : %d'%(len(X_train)))
print('테스트하기 위해 남겨둔 데이터 개수 : %d'%(len(X_test)))

#출력결과
#학습한 데이터 개수 : 480
#테스트하기 위해 남겨둔 데이터 개수 : 207
```



---



## 3일차 - 지도학습(회귀분석)

> 지도학습 두 분석 종류인 회귀분석과 분류분석을 해보자



#### 회귀분석

> 데이터를 가장 잘 설명하는 모델을 찾아서 입력값에  따른 미래 결과값을 예측하는 알고리즘



**어떤 게 좋은 예측일까?**

1. 실제값과 예측값의 차이가 작을수록 좋다?

   1. 실제값-예측값에는 예외가 있음
   2. 그렇다면 차이의 제곱합으로 해보자

2. loss 함수를 이용한다

   1. loss함수가 작을수록 좋은 모델이다
   2. y절편과 기울기값을 조절해서 함수의 크기를 작게 해나가야 한다

3. 함수의 크기를 작게하는 y절편과 기울기를 찾는 방법은?

   1. gradient descent(경사 하강법)

      - 한 번의 계산으로 구하는 게 아니라, 초기값에서 점진적으로 구하는 방ㅎ식
        1. 절편과 기울기를 랜덤하게 초기화
        2. 현재 절편과 기울기값으로 loss값을 계산한다
        3. 어떻게 해야 줄일 수 있는지 알 수 있는 gradient값을 계산한다
        4. 이 값을 활용해서 절편과 기울기값을 업데이트 한다
        5. loss값 차이가 거의 없어질 때까지 2번 ~ 4번 정도 과정을 반복한다(gradient값도 작아짐)

   2. normal equation(least squars)

      - 회귀 분석에서 사용되는 표준 방식 > 실험, 관찰통해서 얻어진 데이터 분석 > 미지 상수 구할 때 사용
      -  이 공식을 통해 일차 함수 기울기와 y절편 구할 수 있음

   3. brute force search

      - 가능한 경우 일일이 탐색
      - 굉장히 오래 걸림
      - 시간복잡도 > O(N^2)

      

**종류**

- 단순 선형 회귀 : 데이터를 설명하는 모델을 직선 형태로 가정 > y절편과 기울기를 구해야 함
  - 특징
    - 가장 기초적이고 많이 사용
    - 입력값이 1개일 때만 적용이 가능하다
    - 입력값과 결과값의 관계를 알아보는데 좋다
    - 영향을 얼마나 미치는 지 알 수 있다
    - 직관적으로 관계를 해석하고 싶을 때 활용한다
- 다중 선형 회귀 : 여러 개 입력값으로 결과값 예측할 때
  - 특징
    - 여러 개 입력값 사이 간 상관관계가 높을 경우 결과 신뢰성 잃을 수 있음



**회귀 평가 지표** : 어떤 모델이 좋은 모델인지 / 실제값과 예측값 차이에 기반한 평가

- RSS
  - 단순 오차 제곱 합
  - 값 작을수록 성능 좋음
  - 가장 간단하고 직관적 해석 가능
  - 오차 그대로 이용 > 입력값 크기에 의존적
  - 절대적 값과 비교 불가능
- MAE,MSE
  - 절대적 크기에 의존한 지표
  - 평균을 그대로 이용하기 때문에 입력값 크기에 의존적
  - 절대적 값과 비교 불가능
  - MSE(mean squared error)
    - 실제값-예측값 > 제곱 > 평균화
    - 예측값과 실제값 차이 면적 합
    - 작을수록 성능 좋음
    - 이상치에 민감(특이값 존재하면 수치가 많이 늘어남)
  - MAE(mean absolute error) 
    - 실제값-예측값 > 절대값으로 변환 > 평균화
    - 작을수록 성능 좋음
    - 변동성 큰 지표와 낮은 지표 같이 예측할 때 굿
- RMSE(root mean squared error)
  - MSE에 루트 씌우기
  - 에러에 따른 손실이 크게 오를 때 굿
- MSLE(mean squared log error)
  - MSE에 로그
- MAPE(mean absolute percentage error)
  - MAE를 퍼센트로
  - 단점은 MAE랑 같음
  - 편향 존재
- R제곱(결정 계수)
  - 결정 계수 : 회귀식이 얼마나 정확한지 나타내는 수
  - 0~1 사이로 >> 0에 가까울수록 정확도가 낮고 / 1에 가까울수록 정확도가 높다
  - 구하는 방법
    - 상관계수 > 제곱
    - 분산분석 데이터 이용(SSR/SST)
  - 1 - RSS/TSS
  - 이것만으로는 의사결정하기 힘듦 > 가설검정을 통해 의사결정(양자택일)



```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
```

```python
X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.2909744,
     5.19692852]
```

```python
#1.X의 형태를 변환 > train_X 저장
#2.Y의 형태를 변환 > train_Y에 저장
train_X = pd.DataFrame(X, columns = ['X'])
train_Y = pd.Series(Y)

# 변환된 데이터를 출력.
print('전 처리한 X 데이터: \n {}'.format(train_X))
print('전 처리한 X 데이터 shape: {}\n'.format(train_X.shape))

print('전 처리한 Y 데이터: \n {}'.format(train_Y))
print('전 처리한 Y 데이터 shape: {}'.format(train_Y.shape))  
```

![image-20220213185346153](MachineLearning_Code.assets/image-20220213185346153.png)

```python
#모델 초기화
lrmodel = LinearRegression()
#train/test
lrmodel.fit(train_X, train_Y)
```

```
linearregression() : 선형회귀

- 가장 기본
- 훈련데이터에 가장 잘 들어맞는 선형 방정식
```

```python
#학습한 결과 시각화
plt.scatter(X,Y) #산점도
plt.plot([0,10], [lrmodel.intercept_, 10*lrmodel.coef_[0] + lrmodel.intercept_], c = 'pink')
plt.xlim(0,10)
plt.ylim(0,10)
plt.title('result')
plt.show()
```

![image-20220213190225412](MachineLearning_Code.assets/image-20220213190225412.png)

```
.coef_ : 추정된 가중치들을 보여줌
.intercept_ : y절편(추정된 상수)
```

```python
lrmode.intercept_  #2.5061811726114125
lrmodel.coef_  #array([0.43078118]) array 형태
beta_0 = lrmodel.intercept_
beta_1 = lrmodel.coef_[0] #계수값(weight값) > 0.4307811782769159
print(beta_0) #2.5061811726114125
print(beta_1) #0.4307811782769159
```



```python
#단순선형회귀 예측
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]

train_X = pd.DataFrame(X, columns=['X'])
train_Y = pd.Series(Y)

lrmodel = LinearRegression()
lrmodel.fit(train_X, train_Y)
```

```python
#train_X 예측(predict)
pred_X = lrmodel.predict(train_X)
print(pred_X)
print(train_Y)
```

![image-20220213194952990](MachineLearning_Code.assets/image-20220213194952990.png)



```python
#다중선형회귀 - 데이터전처리
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score  #평가 지표 / 결정 계수 보겠다
from sklearn.model_selection import train_test_split
```

```python
df = pd.read_csv('./Advertising.csv')
df.head()
```

![image-20220213195140235](MachineLearning_Code.assets/image-20220213195140235.png)

```python
#필요없는 열 제거
df = df.drop(columns = ['Unnamed: 0'])
#info로 확인
df.info()
# 0   FB         200 non-null    float64
# 1   TV         200 non-null    float64
# 2   Newspaper  200 non-null    float64
# 3   Sales      200 non-null    float64
```

```python
#1. sales변수는 label데이터로 y에 저장, 나머지는 x에 저장
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

#2. train/test
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size = 0.2, random_state = 42) #8:2로 

print(train_X)
print(train_Y)
print(test_X)
print(test_Y)
```

```python
#학습시키기
lrmodel = LinearRegression()
lrmodel.fit(train_X, train_Y)

#학습된 파라미터 값 불러오기
beta_0 = lrmodel.intercept_ #y절편(기본 판매량)
beta_1 = lrmodel.coef_[0] #1번째 변수에 대한 계수(FB)
beta_2 = lrmodel.coef_[1] #2번째 변수에 대한 계수(TV)
beta_3 = lrmodel.coef_[2]

print(beta_0)
print(beta_1)
print(beta_2)
print(beta_3)
#2.979067338122629
#0.044729517468716326
#0.18919505423437655
#0.0027611143413671757

#회귀식 >> Y(종속변수) = 0.04*x1 + 0.18*x2 + 0.002*x3 + 2.979
```

```python
#예측
lrmodel.predict(test_X)
#array([16.4080242 , 20.88988209, 21.55384318, 10.60850256, 22.11237326,
#       13.10559172, 21.05719192,  7.46101034, 13.60634581, 15.15506967,
#        9.04831992,  6.65328312, 14.34554487,  8.90349333,  9.68959028,
#       12.16494386,  8.73628397, 16.26507258, 10.27759582, 18.83109103,
#       19.56036653, 13.25103464, 12.33620695, 21.30695132,  7.82740305,
#        5.80957448, 20.75753231, 11.98138077,  9.18349576,  8.5066991 ,
#       12.46646769, 10.00337695, 21.3876709 , 12.24966368, 18.26661538,
#       20.13766267, 14.05514005, 20.85411186, 11.0174441 ,  4.56899622])
```

독립변수 X > feature

종속변수 Y > target

잔차 = 샘플 관측값 - 예측값

```python
#회귀 알고리즘 평가지표_mse, mae
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
```

```python
#train_X, mse, mae 계산
pred_train = lrmodel.predict(train_X)
pred_test = lrmodel.predict(test_X)

mse_train = mean_absolute_error(train_Y, pred_train)
mae_train = mean_squared_error(train_Y, pred_train)

print('MSE_train : %f' % MSE_train)
print('MAE_train : %f' % MAE_train)
#MSE_train : 1.198468
#MAE_train : 2.705129

#train 데이터가 당연히 test 데이터보다 잘나옴
```

```python
MSE_test = mean_absolute_error(test_Y, pred_test)
MAE_test = mean_squared_error(test_Y,pred_test)

print('MSE_test : %f' % MSE_test)
print('MAE_test : %f' % MAE_test)
#MSE_test : 1.460757
#MAE_test : 3.174097
```

```python
#train_X 결정계수(R2)
# 결정계수는 '설명력'
r2_train = r2_score(train_Y, pred_train)
print('R2_train : %f'%R2_train)
#R2_train : 0.895701 >> 89%
```

```python
#test_X 예측값 계산
lrmodel.predict(test_X)

pred_test = lrmodel.predict(test_X)
r2_test = r2_score(test_Y, pred_test)
print('R2_test : %f'%R2_test) 
#R2_test : 0.899438 >> 89%
# >> test가 더 좋네 ? > 언더피팅 
#제일 이상적인 건 train 98%, test95~98%래
```



---



## 4일차 - 지도학습(분류분석)



**분류** : 입력값이 어떤 클래스에 속할 지에 대한 결과값 도출하는 알고리즘



| 트리 구조 기반 | 의사결정나무, 랜덤포레스트..              |
| -------------- | ----------------------------------------- |
| 확률 모델 기반 | 나이브 베이즈 분류기, ..                  |
| 결정 경계 기반 | 선형 분류기, 로지스틱 회귀 분류기, SVM... |
| 신경망         | 퍼셉트론, 딥러닝 모델...                  |
| ..             |                                           |



**의사결정나무**

- 의사결정 규칙을 나무 구조로 나타내서 > 소집단으로 분류 or 예측
- 연속적으로 발생하는 의사결정 문제 시각화 > 이뤄지는 시점과 성과 한 눈에
- 가지치기
  - 가지를 잘라내서 모형 단순화
- 가치분할
  - 나무 가지 생성
- 결정 규칙
  - 분할규칙
    - 새 가지를 어디에서 나오게?
  - 정지규칙
    - 어떻게 해야 새 가지가 더 못나오게 ?
  - 가지치기 규칙
    - 어느 가지를 쳐내야 예측력이 높게?
    - 끝마디 너무 많지 않게
- 훈련용/검정용/시험용
- 특징
  - 노복잡
  - 대용량 데이터 빠르게 가능
  - 비정상적 잡음 데이터에 대해서도 민감함없이 분류 가능
  - 분류 정확도 굿
  - 비모수적 모형(수학적 가정 불필요)
  - 수치형/범주형 변수 모두 사용 가능
- 활용
  - 세분화(segmentation)
    - 비슷한 특성 데이터 몇 개 그룹으로 분할 > 특성 발견
  - 분류(classification, stratification)
    - 목표변수의 범주를 몇 등급으로 나눌 때
  - 차원축소, 변수 선택
  - 예측
  - 교호작용효과의 파악
    - 교호작용 : 두 개 이상 사물이나 현상이 서로 원인-결과가 되는
  - 범주의 병함, 연속형 변수의 이산화
- 구현 단계
  1. 데이터 삽입
  2. 학습/실험 데이터 
  3. 의사결정나무 모형
  4. 분류
  5. 성과 분석
  6. 모형 수정
- 패키지
  - rpart
  - party
  - printcp() : cross validation 계산
  - plotcp() : cross validation을 그래프로 보여주는 함수
  - prune() : 가지치기
  - confusionMatrix(예측값, 실제값)



**오분류표** : 실제 범주와 모형에 의해 예측된 범주 사이 관계

- TP(true positives)
- TN(true negatives)
- FP(false positives)
- FN(false negatives)
- 정밀도
  - TP/(TP+FP)
  - precision
  - 암이라고 예측한 값 중에서 실제로 암일 확률
- 정확도
  - accuracy
  - TP+TN/(TP+FP+FN+TN)
- 재현율 = 민감도
  - recall = sensitivity
  - TP/(TP+FN)
  - 원래 암일 확률에서 암이라고 판단할 확률
- 특이도
  - specificity
  - TN/(FP+TN)



**confusion matrix(오차행렬)** : 실제 클래스와 예측된 클래스 비교

- f1-score



**로지스틱회귀분석**

- 시그모이드 함수
  - s자형 곡선 갖는 수학 함수
  - 가역 함수
  - 역은 로짓함수
  - 실함수로서 미분 가능
  - 모든 점에서 음이 아닌 미분값 가지고, 단 하나의 변곡점 가짐
  - 1차 미분 그래프
  - 0보다 작은 값에서 볼록, 0보다 큰 값에서 오목
- 소프트맥스 함수
  - 시그모이드 함수의 일반화
  - 세 개 이상 분류하는 다중 클래스 분류에서 사용
  - n차원 벡터 입력받아서 각 클래스에 속할 확률 추정
  - 0~1 사이 값으로 정규화 > 출력 값들 총합은 always 1
- 로지스틱회귀 단계
  1. 모델 이용한 예측, 결과값
  2. 예측 결과, 실제 결과값 비교
  3. 예측 정확도 계산



---



## 5일차 - 앙상블



> 앙상블 : 여러 개 분류모형에 의한 결과 종합 > 분류 정확도 높임
>
> 적절한 표본추출법으로 여러 개 훈련용 데이터 집합 만들어서 > 각각 데이터 집합에서 하나의 분류기 결합



**앙상블**

- 과적합 가능성 줄여줌
- 평균 취함 > 편의 제거
- 한 개 모형에서 > 여러 모형 의견 결합하면 변동성 작아짐
- 생긴 이유
  - 의사결정나무에서 분기변수 기준에 따라 분류되는 데이터가 개달라서 불안정
- 기본 형태
  - 부트스트랩 표본추출 > 다수 훈련자료 생성
  - 각 훈련자료에 대해 동일한 알고리즘 > 모형 생성
  - 결과 결합 > 최종 예측치 산출
- 용어
  - 배깅(bagging)
    - 여러 개 부트스트랩 자료 생성
    - 각 부트스트랩 자료 > 예측 모형 > 결합 > 최종 예측 모형
  - 부트스트랩(bootstrap)
    - 동일한 크기 표본 > 무작위 복원추출로
  - 부스팅(boosting)
    - 예측력 약한 애들 결합 > 더 강하게
    - 훈련 오차 빠르고 쉽게 줄이기
    - 예측오차 적어져서 성능 향상

- 랜덤포레스트
  - 발견된 변수 규칙 or 조건문 토대로 나무 구조로 > 분류, 예측

- 분류 분석 모형 평가
  - 교차검증(cross validation)
    - 반복적으로 성과 측정 > 결과 평균
    - 대표적 > k-fold 교차검증
      - 데이터 사이즈 동일한 k개 하부집합으로 나누고 k번째를 검증용, 나머지 k-1개를 훈련용
  - 홀드아웃(hold-out)
    - 랜덤하게 두 분류로 분리 > 교차 검정
  - 부트스트랩
    - 동일한 크기 표본을 랜덤 복원추출로
    - 평가 반복하는 건 교차검증과 비슷, but 훈련용 자료를 반복 재선정
    - 전체 데이터 양 크지 않을 때 가장 적합



---



## 6일차 - 성과분석, 인공신경망분석, 군집분석



**성과분석**

- 홀드아웃
- 교차검증
- 부트스트랩
- ROC curve
  - y축(민감도), x축(1-특이도) 활용해서 평가
  - x,y축 모두 0 일때는 모두 거짓
  - 두 분류 분석 모형을 비교 분석 결과 가시화 가능
- 특징
  - 이익도표(lift chart)
    - 이익 : 개체들이 각 등급에 얼마나 분포하고 있는지
    - 이익도표 : 등급에  따라 계싼된 이익값 누적으로 연결
    - 향상도 곡선 : 랜덤모델이랑 비교 > 해당 모델 성과가 얼마나 향상됐나
      - 상위등급 : 향상도 크고 하위로 갈수록 향상도 감소 > 예측력 적절
      - 등급에 노상관으로 향상도 차이 없으면 > 예측력 안좋음
      - 향상도(lift) = 반응률 / 기본 향상도
      - 좋은 모델 > lift가 빠른 속도로 감소해야



**인공 신경망 분석**

- ANN(artificial neural network)
- 신경망 모형 구축시 고려사항
  - 입력변수(입력 자료 선택에 매우 민감)
    - 범주형 범수 : 모든 범주에서 일정 빈도 이상 값 갖고, 일정할 때
    - 연속형 변수 : 값들의 범위가 변수 간 큰 차이 없을 때
  - 가중치 초기값과 다중 최소값 문제
    - 역전파 알고리즘은 초기값에 따라 결과 많이 달라짐
    - 가중치 0 > 시그모이드 함수 > 선형 > 신경망 모형 > ㄱ근사적으로 선형
    - 초기값은 0근처로 랜덤하게 선택 > 초기 모형은 선형모형
    - 가중치 값 증가 > 비선형모형
- 입력층, 은닉층, 출력층으로 구성
  - 입력층 : 각각 입력변수 1:1로 매칭
  - 입력층, 뉴런 가중치의 결합으로 생성, 은닉층 개수에 따라 복잡도 결정(은닉충 개수 2개 이상 > deep neural network)
  - 출력층 : 뉴런, 가중치 결합으로 생성
    - 종속변수의 형태에 따라 출력층 개수 결정



**군집분석** : 각 개체에 대해 관측된 여러 변수 값 > 유사한 성격으로 군집화 > 파악 > 관계 해석

- 별도 반응변수 노필요
- 유사성에만 기초해서 군집 형성
- 이상값 탐지에 사용
- 계층적 군집
  - 군집 개수 점차 줄여나가기
  - 원하는 개수 군집 형성
  - 군집간 거리 정의 필요
  - 군집수 몰라도 분석 가능
  - 군집 간 거리 측정법
    - 중심연결법
      - 두 군집 중심 간 거리 측정
    - 최단연결법
      - n*n 행렬에서 거리 가장 가까운 데이터 묶어서
    - 최장연결법
      - 거리 먼 데이터나 군집 묶어서
    - 평균연결법
      - 최단 연결법이랑 같은데 평균 사용한다
    - ward 연결법
      - 군집 내 편차의 제곱합 고려
      - 정보 손실 최소화
- 연속형 변수
  - 유클리디안 거리 : 데이터 간 유사성
  - 맨하탄 거리 : 최단 거리
  - 민코우스키 거리 : 맨하탄 + 유클리디안
- 범주형 변수
  - 자카드 거리
  - 자카드 계수
  - 코사인 거리
  - 코사인 유사도
- 비계층적 군집분석 : 사전에 군집수 정해서 군집 할당
  - k-means 군집분석
    - k개 평균 찾기
    - 군집 내 거리 제곱합의 합을 최소화하는 게 목적
    - 잡음, 이상값 영향 있음
- 혼합분포 군집(가우시안 혼합모형)
  - 데이터 > k개 모수적 모형의 가중합으로 표현되는 모집단 모형으로 나왔다고 가정
  - em알고리즘
  - 이상값에 민감 > 사전에 제거해줘야
  - 군집 크기 작으면 > 추정도 저하
    - em 알고리즘
      - e단계(기대치 계산)
      - m단계(기대치 이용, 파라미터 추정)
- som(자기조직화지도)
  - 비지도 신경망
  - 고차원 > 저차원 정렬 > 지도 형태로
  - 위치관계 그대로 보존
  - 입력층, 경쟁층, 가중치, 노드



**연관분석**

- 연관규칙
  - 조건-결과 식으로 표현
  - = 장바구니 분석
  - 대용량 DB 사이에서 변수들 사이 관계 탐색
  - 마케팅 등에서 사용
  - 측정 지표
    - 지지도(support)
      - 상품 두 개 동시 구매할 확률
    - 신뢰도(confidence)
      - a 구매했을 때, b 구매될 확률
    - 향상도(lift)
      - a 구매한 사람이 b 구매할 확률, a 구매 상관없이 b 구매할 확률의 비율
      - if a랑 b 독립 > 향상도 = 1
      - lift > 1 : 관련도 높음
      - lift < 1 : a 구매한 사람은 b 구매안한다는 결론
  - apriori 알고리즘 분석 절차
    1. 최소 지지도 설정
    2. 개별 품목들 중 최소 지지도 넘는 모든 품목 찾기
    3. 두 개 품목 집합 찾기
    4. 결합해서 세 개 품목 집합 찾기
    5. 반복 > 빈발 품목 찾기
