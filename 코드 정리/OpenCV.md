# OpenCV

> opencv를 설치하고
>
> 이를 이용해서 이미지를 데려오고 크기와 색상 등을 조절하는 기초 내용 복습



```python
! pip install opencv-python
```

```python
import cv2
import numpy as np
import sys
cv2.__version__  #4.5.5
```

```python
img = cv2.imread(filename = './fig/puppy.bmp') #이미지 파일 불러와
cv2.namedWindow('image')
cv2.imshow('image', img)   #imshow로 보여주기
cv2.waitKey()              #이것까지 써야 창이 뜸
cv2.distroyAllWindows()    #어떤 키를 누르든 키를 누르면 종료
```

```python
import cv2
import numpy as np
import sys
#보통 창에서 문제가 생기면 커널이 죽어버려서 그냥 임포트 여기에다가 한 번에 씀

img = cv2.imread(filename = './fig/puppy.bmp') #안쓰면 그냥 디폴트 컬러
type(img) #numpy.ndarray
img.shape  #(480, 640, 3)

img2 = cv2.imread(filename = './fig/puppy.bmp',
                flags = cv2.IMREAD_GRAYSCALE)   #grayscale로 하면 
img2.shape  #(480, 640)

img3 = cv2.imread(filename = './fig/puppy.bmp',
                flags = cv2.IMREAD_COLOR)
img3.shape  #(480, 640, 3)

print('image dimension', img.shape)

if img is None:       #만약 파일이 없으면
    print('image read failed')
    sys.exit()        #나와

cv2.namedWindow('image')
cv2.imshow('image', img3)
key = cv2.waitKey()
print(key)                        #아스키 키값이 출력됨
cv2.destroyAllWindows()
```

```python
#사이즈를 줄이고 싶을 땐?
img = cv2.imread('./fig/puppy_jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2) #이렇게 사이즈 줄임
if img is None:
    print('image read failed')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

```python
img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)  #이렇게 쓰면 작아져서 나옴
#print(img.shape)

if img is None:
    print('image read failed')
    sys.exit()

img_re = cv2.resize(img, (320, 240), interpolation = cv2.INTER_AREA)  
#영상 보관 방식(interpolation)
    
cv2.namedWindow('image')
cv2.namedWindow('image_re')
cv2.imshow('image', img)
cv2.imshow('image_re', img_re)
cv2.imwrite('puppy_resize.png', img_re)
cv2.waitKey()
cv2.destroyAllWindows()
```

```python
#창의 위치를 바꾸고 싶을 때
img = cv2.imread('./fig/puppy.bmp', flags = cv2.IMREAD_COLOR)

if img is None:
    print('image read failed')
    sys.exit()
    
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)  # < 이거 안해도 창이 뜨긴 함
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # < 사이즈 왔다갔다 가능
cv2.moveWindow('image',0,0)  #여기서 창의 위치 바꿈
cv2.imshow('image', img)

cv2.waitKey()
cv2.destroyAllWindows()
```

```python
img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)

if img is None:
    print('image read failed')
    sys.exit()
    
cv2.namedWindow('image')
cv2.imshow('image' img)

while True:
    key = cv2.waitKey()
    if key == ord('q') or key == 27:  #q키를 누르거나 esc 키를 누르면
        break
        
cv2.destroyAllWindows()
```

```python
#out창에도 사진이 나오게 
import matplotlib.pyplot as plt

img = cv2.imread('./fig/puppy.bmp', cv2.IMREAD_COLOR)
#bgr 순서(openCV는)
if img is None:
    print('filed')
    sys.exit()
    
cv2.namedWindow('image')
cv2.imshow('image',img)

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #이렇게 bgr을 rgb로 바꿔놔야 사진이 정상으로 나와
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(131), plt.imshow(img), plt.axis('off')
plt.subplot(131), plt.imshow(imgRGB), plt.axis('off')
plt.subplot(131), plt.imshow(imgGray, cmap = 'gray'), plt.axis('off')

plt.imshow(imgGray, cmap = 'gray')  #cmap을 gray로 해줘야 나옴
plt.axis('off')
plt.show()
#rgb로 인식(plt)

while True:
    key = cv2.waitKey()
    if key == 27:
        break

cv2.destroyAllWindows()
```

```python
#for문 돌려서 연속으로 이미지 파일이 나오게
import os

img_list = os.listdir('./fig/images/')
#print(img_list)

img_path = []

for i in img_list:
    img_path_all = './fig/images/' + i
    img_path.append(img_path_all)
#img_path

cv2.namedWindow('image', cv2.WINDOW_NORMAL)              #그냥 전체화면(창은 나옴)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,  #진짜 ㄹㅇ 전체화면으로 뜸(창까지 다 없애서)
                     cv2.WINDOW_FULLSCREEN)

for i in img_path:
    img = cv2.imread(i, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)
    cv2.waitKey(3000)
    
cv2.destroyAllWindows()
```

```python
#for문 말고 무한루프로 나오게 하면서 esc키를 누르면 나오게
idx = 0

while True:
    img_name = img_path[idx]
    img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    
    cv2.imshow('image', img)
    if cv2.waitKey(2000) == 27:
        break
    
    idx += 1
    
    if idx >= len(img_path):
        idx = 0
        
cv2.destroyAllWindows()
```



### 정리

---

resize 할 때

\> `cv2.resize(img, (320, 240), interpolation = cv2.INTER_AREA)`



창의 사이즈를 왔다갔다 조절하고 싶을 때

\> `cv2.namedWindow('image', cv2.WINDOW_NORMAL)`



창의 위치 지정

\> `cv2.moveWindow('image', 0, 0)`    #0,0은 왼쪽 위가 시작



rgb로 바꾸기

\> `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`

\>` cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`



주피터 내에서 사진 나타내기

\> matplot으로

\> `plt.subplot(131), plt.imshow(img), plt.axis('off')`



창은 나오는 전체화면으로 나타내기

\> `cv2.namedWindow('image', cv2.WINDOW_NORMAL)`



창까지 안나오는 완전 전체화면으로

\> `cv2.setWindowProperty('image', cv2.WIND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)`



