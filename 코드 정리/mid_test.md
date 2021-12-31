# 중간고사 문제풀이

> 중간고사 전 간단한 연습문제 풀이



### 1번

**[4,5,6]을 리스트로 넘파이 배열 만들어서 a 변수에 담고 합 구하기**

```python
import numpy as np		#넘파이 호출
a = np.array([4,5,6])	#np.array([]) << 형식
a.sum()					#합 구하기
```



### 2번

**DataFrame([['2,200', '4,300'],['3,400', '1,500']])을 df 변수에 담고**

**천 단위 구분 기호를 제거한 후 모두 숫자로 변경**

```python
import pandas as pd								#판다스 호출
from pandas import Series, DataFrame
df = DataFrame([['2,200', '4,300'],['3,400', '1,500']])
df.applymap(lambda x: int(x.replace(',','')))	#
```



