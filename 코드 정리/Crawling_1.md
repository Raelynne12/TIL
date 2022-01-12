# Crawling

> 크롤링 : 데이터 수집, 분류 >> 주로 인터넷 상의 웹페이지(html, 문서 등) 수집해서 분류하고 저장





### 기본 문법

```python
import pandas as pd
import numpy as np

sample_1 = pd.read_excel('./files/sample_1.xlsx',
                        header = 1,				#헤더를 따로 저장하려면 header = next(data)	
                        usecols = 'A:C',		 #컬럼은 A-C
                        skipfooter = 2,			#밑에 2행은 스킵
                        #names = ['A','B','C'],	 #이름은 A,B,C로 하겠다
                        #dtype = {'입국객수' : np.float64}	#입국객수의 자료형을 float형으로 바꾸겠다
                        )
type(sample_1) 		#dataframe
sample_1.dtypes
#국적코드    object
#성별      object
#입국객수     int64
#dtype: object

#엑셀파일 외에도 직접 주소를 가져오는 것도 가능
fish = pd.read_csv('https://bit.ly/fish_csv', encoding = 'utf-8')
print(fish)
```

```python
sample_1.head()
sample_1.tail()
sample_1.info()

sample_1.index		#RangeIndex(start=0, stop=6, step=1)
sample_1.columns	#Index(['국적코드', '성별', '입국객수', '기준년월'], dtype='object')
sample_1.dtypes		
#국적코드    object
#성별      object
#입국객수     int64
#기준년월    object
#dtype: object
```

```python
sample_1.describe()
sample_1['성별'].value_counts()
#남성    3
#여성    3
#Name: 성별, dtype: int64
sample_1[['국적코드', '성별']]
```

```python
sample_1['기준년월'] = '2019-11'	#열값 바꿈
sample_1[sample_1['성별'] == '남성']	#표로 나옴
condition = sample_1['성별'] == '남성'	#True or False로 나옴

print(condition)
print(~(condition))			#(~())  위의 결과랑 반대
sample_1[condition]
sample_1[~condition]		#[~]
```

