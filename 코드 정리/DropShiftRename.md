# drop/shift/rename



```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#drop
#특정 행, 컬럼 제거
emp = pd.read_csv('./emp.csv')
#scott 퇴사시키기
emp.loc[emp['ename'] == 'scott']
emp.loc[emp['ename'] == 'scott',:]
emp.loc[~(emp['ename'] =='scott,:')]	#not

emp.drop(4, axis = 0)		#행기준, 4번째 인덱스 제외

#예제
#emp 데이터에서 sal 컬럼 제외
emp.drop('sal',axis = 1)
emp.iloc[:,:-1]
emp.drop(['ename','deptno'], axis = 1)
emp.loc[:,'empno':'deptno']

#shift
#행 또는 열 이동
#전일자 대비 증감율
emp['sal'].shift()		#default : axis = 0(행)

#

```

