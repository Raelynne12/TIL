# 중간고사 문제풀이

> 중간고사 전 간단한 연습문제 풀이



### 1번

**[4,5,6]을 리스트로 넘파이 배열 만들어서 a 변수에 담고 합 구하기**

```python
import numpy as np		#넘파이 호출
a = np.array([4,5,6])	#np.array([]) << 형식
a.sum()					#합 구하기
```

---

### 2번

**DataFrame([['2,200', '4,300'],['3,400', '1,500']])을 df 변수에 담고**

**천 단위 구분 기호를 제거한 후 모두 숫자로 변경**

```python
import pandas as pd								#판다스 호출
from pandas import Series, DataFrame
df = DataFrame([['2,200', '4,300'],['3,400', '1,500']])
df.applymap(lambda x: int(x.replace(',','')))	#숫자로 변경 위해 int 삽입
```



```
! applymap 과 map 메소드, 그리고 apply !

pipe() 				>> 테이블 형태로 정리
apply() 			>> 행 or 열로 정리
agg(), transform() 	>> 집합 API
applymap() 			>> 요소별 적용

-----------------------------------------
applymap() 		>> DataFrame에 적용
map() 			>> Series에 적용
```





---

### 3번

**DataFrame(np.arange(1,17)) 을 4행 4열의 행렬로 변환하여 df에 담고 컬럼별 합 구하기**

```python
df = DataFrame(np.arange(1,17).reshape(4,4))
df.sum(axis = 1)		#axis << 축
						#index = 0(행)
						#columns = 1(열)
```

---

### 4번

**atlantis@abc.kr 이메일 주소에서 아이디를 추출 (Series로 변환하여 s 변수에 담은 후 처리)**

```python
s1 = Series(['atlantis@abc.kr'])
vno = s1.str.find('@')					#@ 찾기
#str쓰는 이유 : Series형은 find 사용할 수 없음
list(map(lambda x,y: x[0:y], s1, vno))	#s1[0:vno]
```

---

### 5번

**[1,3,5,15,25] 를 _list 의 변수에 담고 10보다 클 경우, 'pass', 작거나 같은 경우 'fail' 출력**

```python
_list = [1, 3, 5, 15, 25]
for a in _list:				
    if a > 10:				#a번째 요소값이 10이 넘으면
        pass				#패스
    else:					#아니면
        print('fail')		#fail 출력
```

