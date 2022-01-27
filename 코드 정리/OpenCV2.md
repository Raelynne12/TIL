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

