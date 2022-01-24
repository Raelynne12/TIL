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

```
```



