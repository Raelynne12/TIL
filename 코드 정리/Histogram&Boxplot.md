# Histogram

> 1월과 8월의 최고기온과 최저기온을 이용해서 그래프 그리기



```python
#히스토그램 기본

import random
dice = []

for i in range(5):						#반복문 사용해서 5번 수행
    dice.append(random.randint(1,6))	#랜덤함수(1~6까지 랜덤) 값 리스트에 추가
    
print(dice)
plt.hist(dice, bins = 6)				#히스토그램 (bins는 막대 개수)
```

![image-20220105222915002](Histogram.assets/image-20220105222915002.png)

 

```python
import csv
f =  open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)
result = []

for row in data:
  if row[-1] != '':
    result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.hist(result, bins = 100, color = 'r')
```

![image-20220105224140349](Histogram.assets/image-20220105224140349.png)



```python
plt.figure(dpi = 300)
plt.hist(result, bins = 1000, color = 'red')
plt.show()
```

![image-20220105224158694](Histogram.assets/image-20220105224158694.png)



---

### 데이터 이용해서 히스토그램 그리기

```python
#8월과 1월 데이터 출력(최고 기온)

import csv
f = open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)
aug = []		#8월치 넣을 리스트		
jan = []		#1월치 넣을 리스트

for row in data:
    month = row[0].split('-')[1]		#0번째(날짜)를 -로 분할해서 1번째 부분을 month
    if row[-1] != '':					#최고기온이 빈칸이 아니면
        if month == '08':				#그리고 월이 8월이면
            aug.append(float(row[-1]))	#aug 리스트에 실수형 최고기온 추가
        elif month == '01':				#만약 월이 1월이면
            jan.append(float(row[-1]))	#jan 리스트에 실수형 최고기온 추가
            
import matplotlib.pyplot as plt
plt.hist(aug, bins = 100, color = 'lightgreen', label = 'August')	#aug 히스토그램
plt.hist(jan, bins = 100, color = 'lightblue', label = 'January')	#jan 히스토그램
plt.legend()							#라벨 표시
plt.show()								#출력
```

![image-20220105223517605](Histogram.assets/image-20220105223517605.png)



 ```python
 #8월과 1월의 최고기온과 최저기온 모두 나타내기
 
 import csv
 import matplotlib.pyplot as plt
 
 f = open('./seoul_book.csv', encoding = 'cp949')
 data = csv.reader(f)
 next(data)
 aug_high = []		#8월 최고기온 리스트
 aug_low = []		#8월 최저기온 리스트
 jan_high = []		#1월 최고기온 리스트
 jan_low = []		#1월 최저기온 리스트
 
 for row in data:
     month = row[0].split('-')[1]
     if row[-1] != '' and row[-2] != '':
         if month == '08':
             aug_high.append(float(row[-1]))
             aug_low.append(float(row[-2]))
         elif month == '01':
             jan_high.append(float(row[-1]))
             jan_low.append(float(row[-2]))
             
 plt.hist(aug_high, bins = 100, color = 'lightgreen', label = "August_High")
 plt.hist(aug_low, bins = 100, color = 'green', label = 'August_Low')
 plt.hist(jan_high, bins = 100, color = 'lightblue', label = 'January_High')
 plt.hist(jan_low, bins = 100, color = 'blue', label = 'January_Low')
 plt.legend()
 plt.show()
 ```

![image-20220105223950112](Histogram.assets/image-20220105223950112.png)

---

# box plot



```python
import matplotlib.pyplot as plt
import random

result = []

for i in range(13):
	result.append(random.randint(1,1000))

print(result)
print(sorted(result))		#정렬된 거

plt.boxplot(result)
plt.show()
```

![image-20220105224844591](Histogram.assets/image-20220105224844591.png)



```python
import csv
f = open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))		#최고기온 리스트 추가
        
plt.boxplot(result)
plt.show()
```

![image-20220105224702478](Histogram.assets/image-20220105224702478.png)



```python
#8월 1월 최고기온 데이터 박스플롯 출력

import csv
f =  open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
  month = row[0].split('-')[1]
  if row[-1] != '':
    if month == '08':
      aug.append(float(row[-1]))
    elif month == '01':
      jan.append(float(row[-1]))


import matplotlib.pyplot as plt
plt.boxplot([aug,jan])
plt.show()
```

![image-20220105225014008](Histogram.assets/image-20220105225014008.png)



```
! box plot !

맨 위는 최대값
맨 아래는 최소값
박스의 중간은 중위값(2/4)
박스의 위는 3/4값
박스의 아래는 1/4값
동그라미는 이상치(outlier)
```



```python
#월별로 보기

import csv
f =  open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]	#12개 생성

for row in data:
  if row[-1] != '':
    month[int(row[0].split('-')[1])-1].append(float(row[-1]))
    #-1을 하는 이유는 month[]요소는 월-1이어서( 1월>> month[0])

plt.boxplot(month)
plt.show()
```

![image-20220105225834870](Histogram.assets/image-20220105225834870.png)

 

```python
#일별로 보기

import csv
f =  open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

day = []

for i in range(31):
  day.append([])

for row in data:
  if row[-1] != '' :
    if row[0].split('-')[1] == '10':
      day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.boxplot(day)
plt.show()
```

![image-20220105225855355](Histogram.assets/image-20220105225855355.png)



```python
#outlier 제거하기

import csv
f =  open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

day = []

for i in range(31):
  day.append([])

for row in data:
  if row[-1] != '' :
    if row[0].split('-')[1] == '10':
      day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.boxplot(day, showfliers = False)      #outlier 출력 안함
plt.show()
```

![image-20220105230120158](Histogram.assets/image-20220105230120158.png)



```python
#ggplot

import csv
f =  open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

day = []

for i in range(31):
  day.append([])

for row in data:
  if row[-1] != '' :
    if row[0].split('-')[1] == '10':
      day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.style.use('ggplot')						#이 부분 추가해주면 됨
plt.figure(figsize = (10,5), dpi = 300)		

plt.boxplot(day, showfliers = False)    
plt.show()
```

![image-20220105230341774](Histogram.assets/image-20220105230341774.png)