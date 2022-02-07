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

​							 3에 가까우면 산포도가 정규분포에 가까움

```python
df['구매가격'].kurtosis()  #1.3613500036652209
```

