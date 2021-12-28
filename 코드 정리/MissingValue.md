# 결측치 처리

> NA(결측치) 처리



```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1,2,3,np.nan])
s2 = Series(['a','b','c',np.nan])

#NA수정
s1.mean() 		#nan값 제외하고 평균값 산출
s1.fillna(0)	#fillna 사용한 치환 >> 제일 많이 사용함(0으로)
s1.replace(np.nan, 'a')
s1.isnull()		#True or False
s1[s1.isnull()] = 0	#nan값이 0으로 바뀜

#NA로 수정
s3 = Series(['서울','.','대전','.','대구','.','부산'])
s3 = s3.replace('.',np.nan)
print(s3)		#점들이 다 nan으로 변경

#NA를 이전 값 / 이후 값으로 수정
s3.fillna(method = 'ffill')		#NA 앞에 있는 값으로 치환
s3.ffill()						#동일한 방식

#NA를 갖는 행, 열 제거
df1 = DataFrame(np.arange(1,17).reshape(4,4), columns = list('ABCD'))
df1.iloc[0,0] = np.nan
df1.iloc[1,[0,1]] = np.nan
df1.iloc[1,[0,1]] = np.nan
df1.iloc[2,[0,1,2]] = np.nan
df1.iloc[3,:] = np.nan

df1.dropna(how = 'any')		#인덱스에 na가 하나라도 들어가면 다 날라감
df1.dropna(how = 'all')		#인덱스에 na가 모두 다 들어가면 날라감
df1.dropna(thresh = 2)		#Na가 아닌 값이 최소 2개 이상이면 제거하지 않음
df1.dropna(axis = 1, how = 'all')	#특정 칼럼이 모두 NA로만 되어있으면 해당 컬럼 제거
df1.dropna(subset = ['C'])	#C컬럼에 nan값이 있는 행만 제거

#중복값 처리
s1 = Series([1,1,2,3,4])
s1.unique()		#유일한 값 확인

s1.duplicated()	#중복된 값 확인(boolean으로 반환)
s1.drop_duplicates()

df3 = DataFrame({'A':[1,1,3,4], 'B' : [10,10,30,40], 'C' : [100,200,300,400]})
df3.drop_duplicates()
#모든 컬럼의 값이 일치하는 행 제거
df3.drop_duplicates(subset = ['A','B'])   #A랑B
#A,B 컬럼 값이 일치하는 행 제거
df2.drop_duplicates(subset=['A','B'], keep='last')	
#중복되는 거 앞에 거 쓸건지 뒤에 거 쓸건지 
```

