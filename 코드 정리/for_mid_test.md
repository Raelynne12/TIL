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

```
```



