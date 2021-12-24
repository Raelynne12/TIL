# .CSV

> 데이터를 가지고 전처리 과정을 거친 후 원하는 결과물 출력
>
> (csv는 이 과정에서 데이터)



→ [기상자료개방포털 사이트](https://data.kma.go.kr/cmmn/main.do)에서 기온분석 데이터 가져오기

→ 저장 시 파일 형식은 CSV(쉼표로 분리)(*.csv)로 설정



---

# 데이터 전처리

> google colab으로 들어가서 코딩
>
> (jupyter notebook으로 해도 무방)



```python
import csv
f = open('seoul.csv', 'r','encoding = 'cp949')
data = csv.reader(f, delimiter = ',')
print(data)
f.close()
```



1. csv 모듈 불러오기
2. csv 파일을 open()함수로 열어서 f에 저장
   - `r` : read (`w` : write)
   - `encoding = 'cp949`' : cp949라는 형식으로(or utf-8 )

3. f를 reader()함수에 넣어 data라는 csv reader 객체 생성
   - delimiter : 구분자

4. data 출력
5. 2번에서 연 파일 닫기



**출력하기**

```python
import csv
f = open('seoul.csv', 'r','encoding = 'cp949')
data = csv.reader(f, delimiter = ',')
for row in data:
	print(row)
f.close()
```

\-for 반복문을 사용하면 csv 파일에 저장된 데이터 한 줄씩 데려오기 가능

\- 실행 결과를 보면 각 행의 데이터가 `[]`로 구성 → `리스트` → 인덱싱/슬라이싱 가능!

\- 각 행의 데이터가 `''`로 구성 → 문자열 데이터로 구성 → 숫자 비교하려면 변환 필요!



**헤더 저장하기**

```python
import csv
f = open('seoul.csv', 'r','encoding = 'cp949')
data = csv.reader(f, delimiter = ',')
header = next(data)    #4.
print(header) 		   #5.	
f.close()
```

\- 결과 : 헤더(날짜, 지점, 최고기온 등..)

\- 헤더를 별도로 저장할 때 next() 함수 사용

4. 헤더라는 변수에 헤더 데이터 행을 저장
5. header 변수 출력

\- next 함수 : 첫 번째 데이터 행을 읽어오면서 데이터의 탐색 위치를 다음 행으로 이동

```python
import csv
f = open('seoul.csv', 'r','encoding = 'cp949')
data = csv.reader(f, delimiter = ',')
header = next(data)   
for row in data:
	print(row)
f.close()
```

\- 결과 : 헤더를 제외한 나머지(즉 실제 데이터들)



**형변환**

```python
import csv
f = open('seoul.csv', 'r','encoding = 'cp949')
data = csv.reader(f, delimiter = ',')
header = next(data)   
for row in data:
	row[5] = float(row[5])   #최고기온 실수로 변환(문자열로 인식하고 있기 때문)
f.close()
```



---

# 예제

> seoul.csv 데이터 내 최고 기온과 최고 기온이었던 날짜 찾아서 출력하기



**답**

```python
import csv

f = open('./seoul.csv', 'r')
#encoding = 'cp949 / utf-8'
data = csv.reader(f, delimiter = ',')
header = next(data)


#최고기온, 해당하는 날짜

#초기화
max_temp = -9999 
max_date = ''

#print(header)
for row in data:
  #1. 만약 데이터가 누락되어있다면 처리
  if row[5] == '':
    row[5] = -999
  row[5] = float(row[5])
  #2. 비교해서 가장 기온이 높은 날 찾아서 최고기온과 해당되는 일자 찾아
  if max_temp < row[5]:
    max_temp = row[5]
    max_date = row[6]

f.close()
print(max_temp, max_date)
```

\- 자세한 내용은 #확인

```
? 숫자를 초기화할 때 -999를 넣는 이유 ?

최고 기온과 비교를 하기 위해서는 데이터에는 없을 법한 숫자가 들어가야 한다. 때문에 극단적으로 -999라고 한거지, 어떠한 문법이 있는 건 아니다.
```



