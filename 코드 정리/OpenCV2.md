## 키, 마우스, 트랙바로 컨트롤하기



### 1) 키

---

```python
img = cv2.imread('./fig/cat.bmp', 0)

if img is None:
    print('failed')
    sys.exit()
    
img1 = img.copy()

cv2.imshow('image', img)

while True:
    key = cv2.waitKey()
    
    if key == 27:
        break
    elif key == ord('e'):
        cv2.Canny(img, 50, 150)
        cv2.imshow('image', img)
        
    elif key == ord('i'):
        img = 255 - img
        cv2.imshow('image', img)
        
    elif key == ord('r'):
        img = img1.copy()
        cv2.imshow('image', img)  #리셋할 때는 copy를 이용해서 해야
        
cv2.destroyAllWindows()
```



### 2) 마우스

---

```python
def call_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:     	#누를 때 좌표
        prnt('left button down : ', x, y)
    elif event == cv2.EVENT_LBUTTONUP: 		#눌렀다가 뗐을 때 좌표
        print('left button up : ', x, y)
    elif e vent == cv2.EVENT_MOUSEMOVE:		#움직일 때 좌표들 다 나옴
        if flags == cv2.EVENT_FLAG_LBUTTOM:	#이렇게 써야 눌렀을 때 상태의 좌표들만 나옴(클릭 후)
            print(x,y)

img = np.ones((480,640,3), np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', call_mouse, img) 
#어느 창에서 받을 건지 / 이 함수를 호출해라 / 인자
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

```python
#마우스로 그림 그려보기
oldx = oldy = 0
def call_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:     	#누를 때 좌표
        prnt('left button down : ', x, y)
    elif e vent == cv2.EVENT_MOUSEMOVE:		#움직일 때 좌표들 다 나옴
        if flags == cv2.EVENT_FLAG_LBUTTOM:	#이렇게 써야 눌렀을 때 상태의 좌표들만 나옴(클릭 후)
            cv2.line(img, (oldx, oldy), (x, y), (250,10,10), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y #0으로 가면 0이랑 이어져서 이상해짐

img = np.ones((480,640,3), np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', call_mouse, img) 
#어느 창에서 받을 건지 / 이 함수를 호출해라 / 인자
cv2.imshow('image', img)
while True:
    
    key = cv2.waitKey()
    
    if key == 27:
        break
    
    elif key == ord('w'):
        cv2.imwrite('./fig/sign.jpg', img)  #저장
        

cv2.destroyAllWindows()
```



### 3) 트랙바 나타내기

---

```python
def call_trackbar(pos):
    img[:] = pos
    cv2.imshow('image', img)
    
img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 50, 255, call_trackbar) #최대값은 항상 255
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

```python
#선글라스 이미지가 트랙바로 나타나게

def trackbar(pos):
    global mask
    img_glass = mask*pos   #여기가 왜 이런 건지는 아직 이해가 안됨(내일 설명해주신대)
    cv2.imshow('mask', img_glass)
    
img = cv2.imread('./fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)
mask = img[:,:,-1]

mask[mask > 0] = 1  #여기 부분도 잘 이해가 안 감 아직까지

cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.imshow('mask',mask)
cv2.createTrackbar('level', 'mask', 0, 255, trackbar)
cv2.waitKey()
cv2.destroyAllWindows()
```

