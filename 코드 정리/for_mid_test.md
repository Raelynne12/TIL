# 시험 대비 문제 복습(Pandas)

> 시험 대비 4문제 리뷰



### 1번

**radius_mean, texture_mean, texture_se, smoothness_se 가 NA인 행 제거하고 총 행 수 리턴**

```python
vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull() 
#네 컬럼 모두 NA값이 나오는 부분 vbool에 입력

vbool.sum() 		#vbool의 합 = 컬럼 네 개가 모두 NA인 행의 수 
df1.loc[vbool,:]	#컬럼 네 개가 모두 NA인 행 확인 << loc사용

###제거###
#1번째 방법
mrow = df1.shape[0] - vbool.sum()		#전체 행 개수 - NA인 행 개수 / shape[0]:행개수
prin(mrow)

#2번째 방법
nrow = df1.dropna(subset = ['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how = 'all').shape[0] #이 네 컬럼에 NA값 모두 있으면 제거
										#shape[0]을 써줘야 총 행수가 나옴
print(nrow)

```

---

### 2번

**concavity_mean의 standard scaling(표준화) 후,결과가 0.1 이상인 값의 개수 출력**

```python
#1) standard scailing(표준화) = (원 데이터 - 평균) / 표준편차
#2) minmax scailing(정규화) = (원 데이터 - 최소) / (최대 - 최소)
df1.columns
vscale = (df1['concavity_mean'] - df1['concavity_mean'].mean()) / df1['concavity_mean'].std()	

(vscale > 0.1).sum()		#0.1이상인 값의 개수 출력
```

```
! scailing !

-머신러닝을 위한 데이터셋을 정제할 때, 특성별로 데이터의 스케일이 다르면 잘 동작하지 않을 수 ㅇ
-스케일링을 통해 모든 특성의 범위(분포)를 동일하게 만들어줘야함
→ 특성 스케일링 / 데이터 스케일링

<<표준화 standardization>>
특성들의 '평균'이 0, '분산'이 1인 가우시안 정규분포를 가진 값으로 스케일링
→ 특성들을 정규분포로

<<정규화 normalization>>
특성들을 '특정 범위'(주로 0,1)로 스케일링
→ 가장 작은 값은 0, 큰 값은 1로 변환 
```

---

### 3번

**texture_se의 상위 10%값(NA를 제외한 건수의 10%)를 이상치로 가정, **

**10%를 제외한 값의 최대값으로 수정하고 평균을 소수점 둘째자리로 반올림**

```python
#이상치 건 수 확인
df1['texture_se'].dropna().shape[0]		#565(행 개수)
nx = int(np.trunc(df1['texutre_se'].dropna().shape[0]*0.1))	#56
#np.trunc() >> 소수점 그냥 버려버림

#이상치를 제외한 나머지 >> 평균
vrank = df1['texture_se'].rank(ascending = False, method = 'first')
#rank함수 안에는 NA값 자동으로 안넣어서 dropna안써도 됨
#ascending = False는 내림차순, method = 'first'는 동점자 처리할 때 첫 번째로 나온 애가 1
df1.loc[vrank > nx, 'texture_se']	#정상치 데이터
df1.loc[~(vrank>nx), 'texture_se']	#이상치 데이터
df1.loc[vrank <= nx, 'texture_se']	#이상치 데이터

#정상치 데이터 최대값
vamx = df1.loc[vrank > nx, 'texture_se'].max()
df1['texture_se'].sort_values(ascending = False)[:nx]
#sort_index는 인덱스 기준 / sort_values는 컬럼 기준
#[:nx]는 NA값 제외

#이상치 데이터를 vmax 치환
df1.loc[vrank <= nx, 'texture_se'] = vmax
round(df1['texture_se'].mean(),2)	#소수 둘 째자리까지 평균
```

```
! 이상치(Outlier) !

-전체 데이터의 패턴에서 벗어난 이상값을 가진 데이터
-모델의 성능에 영향을 받기 쉬우므로 해결해야

<<IQR>>  (이상치 판단 방법 중 하나)
사분위 값의 편차를 이용하는 방법(박스플롯 방식으로 시각화 가능)
Q3-Q1인 IQR에 1.5를 곱해서 최소 최대값을 정한 뒤, 이 값을 넘어서는 데이터를 이상치로 간주
```

---

### 4번

**symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로 반올림**

```python
from numpy import nan as NA

df1['symmetry_mean'] = df1['symmetry_mean'].replace('-', NA)

#최소값 확인
df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')	#float 형태로 
vmin = df1['symmetry_mean'].min()							#최소값 찾기

#결측치 수정
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)	#NA값은 최소값으로 대체
round(df1['symmetry_mean'].mean(),2)
```

---

### 참고

```python
_df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'JANG','MIN', 'SHIN'],
     'age': [24, 31, 25, 17, np.nan]})

#동점자 처리 기준 5가지
_df['rank_average'] = _df['age'].rank(method='average')	#default
_df['rank_min'] = _df['age'].rank(method='min')
_df['rank_max'] = _df['age'].rank(method='max')	#큰 값부터 하니까 1이 아니라 둘 다 2
_df['rank_first'] = _df['age'].rank(method='first')	#첫 번째로 나온 애가 1등
_df['rank_dense'] = _df['age'].rank(method='dense')	#min과 유사
```

