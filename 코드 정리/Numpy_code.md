# Numpy

> NUMerical PYthon



### 일반 리스트와 넘파이의 차이

```python
#일반 리스트로
import matplotlib.pyplot as plt
t = []
p2 = []
p3 = []

for i in range(0,50,2):
    t.append(i/10)
    p2.append((i/10) ** 2)
    p3.append((i/10) ** 3)
    
plt.plot(t, t, 'r--', t, p2, 'bs', t, p3, 'g^')
plt.show()
```

![image-20220106225251414](Numpy_code.assets/image-20220106225251414.png)

```python
#넘파이 사용시
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.,5.,0,2) 	#0이상 5미만 구간, 0.2 간격으로 실수 생성
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

![image-20220106225434692](Numpy_code.assets/image-20220106225434692.png)

​                      				

​								*** "결과적으로는 차이가 없지만, 코드가 간결하고 for문이 없어서 빠름"***		



---

### numpy 라이브러리의 함수

```python
import numpy as np
print(np.sqrt(2))		#제곱근
print(np.pl)			#원주율
print(np.sin(0))		#싸인
print(np.cos(np.pi))	#코싸인
```

```python
#random 함수
a = np.random.rand(5)	#0과 1사이 n개 실수 5개 반환 / randint << 정수 반환
print(a)
print(type(a))			#리스트와 유사한 배열

print(np.random.choice(6,10))	#1~5까지 숫자를 10번 랜덤 선택
print(np.random.choice(6,10, replace = False))	#'중복 없이'

print(np.random.choice(6,10, p = [0.1,0.2,0.3,0.1,0.2,0.1])) #확률 설정 >> 합 1
```



---

### 라이브러리 이용해서 그래프 그리기

```python
#버블 차트
import matplotlib.pyplot as plt
import random

x = []
y = []
size = []

for i in range(200):
    x.append(random.randint(10,100))	#10~100 사이 랜덤 정수 x에 추가
    y.append(random.randint(10,100))
    size.append(random.randint(10,100))
    
plt.scatter(x,y, s = size, c = x, cmap = 'jet', alpha = 0.7)
plt.colorbar()
plt.show()
```

![image-20220106232029675](Numpy_code.assets/image-20220106232029675.png)



```python
#numpy 활용
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(10, 100, 200)  # 10 이상 100 까지 정수 200개
y = np.random.randint(10, 100, 200)
size = np.random.rand(200) * 100 # 0에서 1 사이의 200개의 실수(float)를 만들고 * 100
    
plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()
```

![image-20220106232405663](Numpy_code.assets/image-20220106232405663.png)



---

### numpy array 생성

```
```

