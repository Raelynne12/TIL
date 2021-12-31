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



