# 자료구조

> 자료구조 - 자료를 효율적으로 관리하는 방법
>
> 알고리즘 - 목적지까지 최적의 이동 경로를 찾는 방법



자료구조 종류

- 단순 자료구조
  - 정수, 실수, ...
- 선형 자료구조
  - 리스트
  - 스택
  - 큐
- 비선형 자료구조
  - 트리
  - 그래프
- 파일 자료구조
  - 순차 파일
  - 색인 파일
  - 직접 파일



# Algorithm

> 알고리즘 성능 분석 방법 >> 시간 복잡도(Time Complexity)
>
> 알고리즘 성능 표기법 >> 빅-오 표기법(O(f(n))) 형태
>
> 자료구조 >> 알고리즘 >> 프로그래밍 언어 >> 소프트웨어



### 기본 코드

```python
# 함수 부분


# 전역 변수 부분


# 메인 코드 부분
katok = ['다현', '정연', '쯔위', '사나', '지효']
katok.append(None)			#빈칸 추가
katok[5] = '모모'
print(katok)
#출력 결과
#['다현', '정연', '쯔위', '사나', '지효', '모모']

katok.append(None)
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
katok[3] = '미나'
print(katok)
#출력 결과
#['다현', '정연', '쯔위', '미나', '사나', '지효', '모모']
```

---

### 함수 코드

```python
# 함수
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    katok[position] = None
    kLen = len(katok)
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])
    
# 전역
katok = []

# 메인
add_data('기연')
add_data('정현')
add_data('지원')
add_data('선아')
add_data('이지')
print(katok)

insert_data(2,'은지')
print(katok)

delete_data(3)
print(katok)
```

