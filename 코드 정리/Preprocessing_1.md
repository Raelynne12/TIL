# 기본 그래프 그리기



### 선 모양 바꾸기

```python
import matplotlib.pyplot as plt

plt.title('linestyle')		#제목 설정
plt.plot([10,20,30,40], color = 'r', linestyle = '--', label = 'dashed')
plt.plot([40,30,20,10], c = 'g', ls = ':', label = 'dotted')
plt.legend()				#범례 표시
plt.show()
```

![출력 결과](Preprocessing_1.assets/image-20211229003944516.png)



### 마커 모양 바꾸기

```python
plt.title('marker')
plt.plot([10,20,30,40], 'r.', label = 'circle')
plt.plot([40,30,20,10], 'g^', label = 'triangle up')
plt.legend()
plt.show()
```

![image-20211229004157441](Preprocessing_1.assets/image-20211229004157441.png)



### 최고기온 그래프 그리기

```python
import csv
import matplotlib.pyplot as plt
f = open('./seoul_book.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)
result = []

for row in data:
	if row[-1] != '':
		result.append(float(row[-1]))
print(result)		#최고기온 모아놓은 리스트 출력
plt.plot(result, 'skyblue') #리스트를 그래프로
plt.show()
```

![image-20211229004905111](Preprocessing_1.assets/image-20211229004905111.png)



### 내 생일의 기온변화를 그래프로 그리기

```python
for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '10' and row[0].split('-')[2] == '30':
            result.append(float(row[-1]))
plt.plot(result, 'pink')
plt.title("My Birthday's temperature")
plt.show()
```

![image-20211229005423335](Preprocessing_1.assets/image-20211229005423335.png)