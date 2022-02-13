# 통계 기초 - 실습

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import chisquare
from scipy import stats
import scipy as sp
import statsmodels.api as sm
from statsmodels.formula.api import ols, logit, glm
```

```python
df = pd.read_csv('./spstat1.csv', sep = ',', encoding = 'euc-kr')
df[(df['구매가격'] > 150) & (df['구매가격'] < 200)]
```

![image-20220207204031388](Statistics_01.assets/image-20220207204031388.png)



## 기술통계

> 측정이나 실험에서 수집한 자료의 정리, 요약, 해석, 표현 등을 통해 자료의 특성을 규명



통계 > **데이터를 다루는 목적** > 2가지

1. 기술통계(desciptive statistics)  >> desciptive : 묘사하는, 설명하는(not technique)
2. 추리통계(inferential statistics)

(추리통계는 다음 시간에...)



기술 통계 **기법 **> 2가지

1. 데이터의 집중화 경향에 대한 기법
   - 수집한 데이터를 대표하는 값이 무엇인지, 어떤 값에 집중되어 있는지
   - 평균(mean), 중앙값(median), 최반값(mode) 등
2. 분산도 기법
   - 수집한 데이터가 어떻게 퍼져있는지
   - 뭉쳐있는지, 퍼져있는지
   - 표준편차(standard deviation), 사분위(quartile) 등



**kurtosis**(첨도) : 확률분포의 꼬리가 두꺼운 정도를 나타냄(극단적 편차나 이상치가 많을수록 값 커짐)

​							 =확률분포의 뾰족한 정도(얼마나 평균에 몰려있는가)

​							 3에 가까우면 산포도가 정규분포에 가까움

​							 >3이면 완만한 분포, <3이면 더 뾰족한 분포

```python
df['구매가격'].kurtosis()  #1.3613500036652209
```

**skewness**(왜도) : 분포의 비대칭도(어느 짝으로 쏠렸냐)

​								왜도 0 : 정규분포

​								왜도 > 0 : 왼쪽으로 치우침

​								왜도 < 0 : 오른쪽으로 치우침

```python
df['구매가격'].skew()     #0.8074518614845148
```



```python
df['사용브랜드'].value_counts()  #각 몇 개인지
```



`%matplotlib inline` > IPython에서 제공하는 rich output(그림, 소리..)에 관한 표현방식

\>> notebook 브라우저 안에서 바로 그림을 볼 수 있게 해줌



```python
df['사용브랜드'].replace([1,2],['삼성','애플']).value_counts().plot(kind = 'bar')
```

![image-20220207210421374](Statistics_01.assets/image-20220207210421374.png)



**T검정** : 검정통계량이 정규분포를 따르며 분포와 관련된 스케일링 변수값들이 알려진 경우에 사용

​			 간편하게 평균을 비교할 수 있는 통계 가설 검정

​			 모집단의 분산이나 표준편차를 알지 못할 때 표본으로부터 추정된 분산이나 표준편차로 검정

1. 두 모집단 평균 간의 차이는 없다 >> 귀무가설

   - 버려질 것으로 예상되는 가설

   - t검정 이후 가설을 수용할지, 기각할지 결정

2. 두 모집단 평균 간의 차이가 있다 >> 대립가설

중 하나를 선택

특징

- 독립된 두집단의 평균 차이가 있는지 검사하는 방법
- 30개 이하의 적은 수의 표본에 대해 활용
- 모집단의 표준편차를 알 수 없을 때 사용 > 모집단의 표준편차 대신 표본의 표준편차 사용



**T값**(t-value) : t검정에 이용되는 검정통계량, 두 집단의 차이의 평균을 표준오차로 나눈 값

​					    t값이 커져서(평균차이가 있을 가능성이 커져서) 기각역에 존재하여 유의확률(p-value)이 						0.05보다 작으면 평균 차이가 유의미한 것으로 해석됨 >> 귀무가설 기각



**T분포** : 평균이 0, 좌우 대칭을 이루며, t값이 커질수록 표준정규분포와 같은 형태



기각역 > 단측검정일 때는 하나 존재 / 양측검정일 때는 두 개 존재

유의확률(p-value) : 귀무가설이 맞다고 가정할 때 얻은 결과보다 극단적인 결과가 실제로 관측될 확률



```python
mean1 = df[df['사용브랜드'] == 1].구매가격.values #브랜드가 삼성인 것들의 구매가격 값들
mean2 = df[df['사용브랜드'] == 2].구매가격.values
```

```python
%matplotlib inline
sns.distplot(mean1, kde = True, fit = sp.stats.norm) #커널 데스티네이션(커널 밀도 함수)
sns.distplot(mean2, kde = True, fit = sp.stats.norm) #fit > 튜플을 pdf형태로 받아서 그리드형태로 그려줌
plt.show()
sp.stats.shapiro(mean1)
```

![image-20220208011448788](Statistics_01.assets/image-20220208011448788.png)



**교차분석**(카이제곱 검정) : 질적 독립변수와 질적 종속변수의 관계를 보기 위한 분석

​											 ex) 거주지역과 성별간 관계를 알아보고 싶을 때 쓰는 방식

```python
pd.crosstab(df['월수입'],df['사용브랜드'])
```

![image-20220207235620753](Statistics_01.assets/image-20220207235620753.png)

```python
#chi2_contingency()
result = pd.crosstab(df['월수입'], df['사용브랜드'])
stats.chi2_contingency(observed = result)
#카이제곱 값 : 12.86516581745558
#p-value : 0.024675611662926037  < 0.05
#0.05보다 작으니까 통계적으로 유의미한 차이가 있음 >> 귀무가설 기각
#월수입에 따라 사용브랜드 차이가 있음

#5가 나온거는
#df(자유도, degree of freedom) : k-1(=6-1) >> 5
#자유도 : 자유롭게 변할 수 있는 원소의 개수

#array : 기대치(expected value)
```

```python
#결과값
#(12.86516581745558,
# 0.024675611662926037,
# 5,
# array([[16.63095238, 16.36904762],
#        [18.14285714, 17.85714286],
#        [26.20634921, 25.79365079],
#        [18.6468254 , 18.3531746 ],
#        [20.15873016, 19.84126984],
#        [27.21428571, 26.78571429]]))
```



레빈테스트 : 둘 이상의 그룹에 대해 계산된 변수에 대한 분산의 동등성을 평가하는 데 사용



비교하고픈 그룹이 3개 이상일 때 분석하는 방법 >> 분산분석(ANOVA), kruskal-wallis test

|          | 모수적 방법 | 비모수적 방법          |
| -------- | ----------- | ---------------------- |
| 2개      | T-test      | wilcoxon rank sum test |
| 3개 이상 | ANOVA       | kruskal-wallis test    |

(모수 : 모집단의 모평균, 모표준편차, 모분산 등)

\- 모수적 방법과 비모수적 방법은 정규성 가정을 만족하는지 여부에 따라 나뉨



**가정 검토**

1. 정규성 가정
   - 표본의 크기가 충분히 크지 않은데 모집단이 정규분포를 따르는지 모를 때 사용하는 검정
   - 내가 뽑은 표본이 정규분포를 따르는 모집단에서 나온 건지 아닌지 판단
   - p-value < 0.05여야 가정 충족
2. 등분산 가정
   - 등분산 = 그룹 간 분산 같다
   - p-value가 > 0.05 여야 가정 충족
   - 그룹간 변동과 그룹내 변동을 이용해서 분석
   - 그룹간 변동 > 그룹내 변동 하다면, 그룹 간 차이가 존재한다고 검정
   - 등분산 가정을 확인하는 검정 >> levene's test(레빈의 검정), bartlett's test(바틀렛 검정)



**레빈의 등분산 검정**

\- 집단 간 분산이 같은지 다른지 여부 알아 볼 때, oneway ANOVA 실시 전 가정에서 확인 용도 등

   bartlett과 달리 표본이 정규성을 보이지 않아도 사용 가능

​	분포 특성에 따라 대표값을 평균, 중앙값, 절사평균값 셋 중 하나로 설정 > 검정

   평균을 대표값 > 정규분포처럼 좌우 대칭, 한 쪽으로 치우치지 X

   중앙값을 대표값 > 카이제곱분포처럼 표본 분포가 한 쪽으로 치우쳐져 있을 때

   절사평균을 대표값 > 표본 분포가 코시분포와 같이 꼬리가 두꺼운 경우

```python
sp.stats.levene(mean1, mean2)
#LeveneResult(statistic=13.443717170975082, pvalue=0.00030027808643848084)
```

```python
#t-test
stats.ttest_ind(mean1, mean2, equal_var = False) #equal_var : 등분산이 같냐
#pvalue=3.598124628532717e-17) >> 두 집단 간 차이 있음
```



**다음날 복습한 내용**

```python
mean = df['재구매의향'].values
mean1 = df[df['사용브랜드'] == 1].재구매의향.values
mean2 = df[df['사용브랜드'] == 2].재구매의향.values

%matplotlib inline
sns.distplot(mean1, kde = False, fit = sp.stats.norm)
sns.distplot(mean2, kde = False, fit = sp.stats.norm)
plt.show()
sp.stats.shapiro(mean1)
#결과가 0.05보다 작으므로 >> 통계적으로 유의
```

![image-20220209010224534](Statistics_01.assets/image-20220209010224534.png)



```python
sp.stats.levene(mean1, mean2)
#LeveneResult(statistic=0.1179597504462619, pvalue=0.7315465812585951)
#p-value가 0.05보다 크므로
#귀무가설(등분산 가정 기각 못함 > 가정 충족함)

#independent 2 sample > t test
stats.ttest_ind(mean1, mean2, equal_var = True) #등분산 가정
#pvalue=0.9290258377820513) > 0.05 : 귀무가설 기각 못함(가정 충족) > 유의미한 차이 없음
```

 

```python
#2 개 이상일 때는 t test 대신 anova
#귀무 : 3집단 평균 다 같다
#대립 : 3집단 평균 다 같지 않다
#p-value <0.05 : 귀무가설 기각하고 대립가설 채택
#요인분석 > 3개
anova1 = df[df['연령2'] == 1].재구매의향.values
anova2 = df[df['연령2'] == 2].재구매의향.values
anova3 = df[df['연령2'] == 3].재구매의향.values
```

```python
sns.distplot(anova1, kde = False, fit = sp.stats.norm)
sns.distplot(anova2, kde = False, fit = sp.stats.norm)
sns.distplot(anova3, kde = False, fit = sp.stats.norm)
plt.show()
```

![image-20220214004229317](Statistics_01.assets/image-20220214004229317.png)

```python
stats.f_oneway(anova1, anova2, anova3)
#pvalue=1.613686022426391e-25) : <0.05 
#HO : 연령2의 세 집단간 재구매의향은 차이가 없다 > 통계적으로 유의하게 나온 거니까
#세 집단 간 모두 차이가 없다고 말할 수 없다 > 사후테스트 필요(어떤 수준에서 평균 차이 나는지)
```

```python
#사후분석
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tucky = pairwise_tukeyhsd(endog = df['재구매의향'], #데이터
                         groups = df['연령2'],      #그룹
                         alpha = 0.05)              #유의수준(significant level)
tucky.summary()
#meandiff > 평균차이 > 두 세 번째 행은 차이가 좀 있네
#p-adj > 조정된 pvalue
#reject > 귀무가설 기각

#결과 해석
#1-3, 2-3 집단 간 평균 차이 존재 : p-value = 0.001 > 귀무가설 기각(reject = True)
```

![image-20220214004301362](Statistics_01.assets/image-20220214004301362.png)

```python
tucky.plot_simultaneous()
plt.vlines(x = 49.57, ymin = -0.5, ymax = 4.5, color = 'yellow')
plt.show()
#1,2 집단은 붙어있는데 3집단은 떨어져있음
```

![image-20220214004323599](Statistics_01.assets/image-20220214004323599.png)

```python
#연령에 따른 구매가격 차이
anova1 = df[df['연령2'] == 1].구매가격.values
anova2 = df[df['연령2'] == 2].구매가격.values
anova3 = df[df['연령2'] == 3].구매가격.values

stats.f_oneway(anova1, anova2, anova3)
#일원분산분석 ㄱㄹ과 f통계량은 0.818,  pvalue=0.44245014422691564 > 0.05
#세 집단 간 유의한 차이가 없음
```

```python
sns.distplot(anova1, kde = False, fit = sp.stats.norm)
sns.distplot(anova2, kde = False, fit = sp.stats.norm)
sns.distplot(anova3, kde = False, fit = sp.stats.norm)
plt.show()
#다 평균에 몰려있네
```

![image-20220214004351930](Statistics_01.assets/image-20220214004351930.png)

```python
#상관분석
#피어슨 상관계수
sp.stats.pearsonr(df.재구매의향, df.구입조언)
#(0.41783620648818565, 4.546075388272401e-12)

corr = sp.stats.pearsonr(df.재구매의향, df.구입조언)
print('상관관계 = %.2f, p-value = %.2f'%(corr))
#상관관계 = 0.42, p-value = 0.00

df.corr(method = 'pearson') #상관행렬표 > 자기 자신은 1 
#절대값이 1에 가까울수롭 상관관계 있다고 보고 뽑아서 패턴 분석
#상관관계 중요
```

![image-20220214004440592](Statistics_01.assets/image-20220214004440592.png)

```python
#회귀분석
ols(formula='재구매의향 ~ 성별+연령+학력+월수입+사용기간+구매가격+구입조언+브랜드이미지+가격만족도+구매중요도1_메모리+하루사용시간', data=df).fit().summary()
#~ 다음 . 하면 전체 다 가져옴
#fit() > fitting 
#r-squared > r2 > 결정계수
#가능도가 높을수록 정규에 가까워짐(log-likelihood)
#aic, bic > 낮을수록 좋음
#p>|t| < 0.05 : p-value
#회계식
#y = 0.1292*사용기간 + 0.1206*구입조언 + 0.4527*브랜드이미지+0.3961*가격만족도+ -0.1580
```

```python
sns.lmplot(y = '재구매의향', x = '사용기간', data = df)
```

![image-20220214004520181](Statistics_01.assets/image-20220214004520181.png)



---

(복습)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import chisquare
from scipy import stats
import scipy as sp
import statsmodels.api as sm
from statsmodels.formula.api import ols, logit, glm
```

```python
df = pd.read_csv('./spstat1.csv', sep = ',', encoding = 'euc-kr')
df.head()

#at
df.at[5, '구매가격'] #구매가격 열의 5번째 행 값 

df[(df['구매가격']>150) & (df['구매가격']<200)].head(5)
```

```python
#기술통계
#측정, 실험에서 수집한 자료, 데이터 정리하고 해석
#not technique, it's descriptive(묘사하는, 그려서 설명하는)

#kurtosis : 첨도(꼬리의 두꺼운 정도) > 클수록 이상치 많음(or 편차 큰)
# 3에 가까우면 산포도가 정규분포에 가까움
# >3이면 완만한 분포, <3이면 더 뾰족한 분포
df['구매가격'].kurtosis()
#1.3613500036652209

#skew : 왜도
#분포의 비대칭도(어느 짝으로 쏠렸냐)
#0이 정규
#>0 왼쪽으로, <0 오른쪽으로
df['구매가격'].skew()
#0.8074518614845148

%matplotlib inline
df['사용브랜드'].replace([1,2], ['삼성','애플']).value_counts()
#삼성    127
#애플    125
#Name: 사용브랜드, dtype: int64

df['사용브랜드'].replace([1,2], ['삼성','애플']).value_counts().plot(kind = 'bar')
```

![image-20220214003809366](Statistics_01.assets/image-20220214003809366.png)

```python
#교차분석
pd.crosstab(df['월수입'],df['사용브랜드'])
```

![image-20220214003847310](Statistics_01.assets/image-20220214003847310.png)



