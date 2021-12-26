# Pandas

> (panel datas)
>
> pandas는 데이터 조작 및 분석을 위한 python 프로그래밍 언어 용으로 작성된 sw library
>
> 특히 숫자 테이블과 시계열 조작하기 위한 데이터 구조와 연산 제공
>
> \* pandas는 파이썬 데이터 분석에 제일 많이 사용



1차원 배열 형태 데이터 구조 : `Series`

2차원 배열 형태 데이터 구조 : `DataFrame`



---

### Series

```python
#기본 메소드 : 벡터 연산 불가능(매 원소마다 반복 불가)
l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']
list(map(lambda x: x.upper(),l1))   #l1.upper()는 X
list(map(lambda x:x.split('/'), l2))
#출력결과
#['ABC','DEF']
#[['a', 'b', 'c'], ['d', 'e', 'f']]
```

```python
#pandas 메소드 : 벡터화 내장(매 원소마다 반복 가능)
from pandas import Series, DataFrame

#찢기
Series(l1)
s1 = Series(l1)
s2 = Series(l2)
s2.str.split('/')   #str해야됨(문자열)
#출력결과
#0    [a, b, c]
#1    [d, e, f]

#대소치환
s1.str.upper()
s1.str.lower()

#replace(치환)
s1.str.replace('a','A')
s1[s1.str.startswith('a')]
s1[s1.str.endswith('c')]
s1[s1.str.contains('e')]
#출력결과
#0    abc
#dtype: object
#0    abc
#dtype: object
#1    def
#dtype: object
```



**1000단위 구분기호(,) 없애고 합 구하기**

```python
#예제
#천단위 구분기호 처리 + 합

s3 = Series(['1,200','3,000','4,000'])
s3.str.replace(',','').astype('int').sum()  
#replace로 쉼표 빼고, astype으로 정수형 바꾸고, sum으로 합

#출력결과
#8200
```



**문자열**

```python
#문자열 크기(len)
s1.str.len()

Series(['aaba','abcsava']).str.count('a')  #count 포함되어 있는 개수
Series(['   a', '  d  dw']).str.strip()    #공백 제거

Series(['aaaabaaca','abababaav']).str.strip('a') #중간값 삭제 불가, 양 끝만 삭제
Series(['aaaabaaca','abababaav']).str.replace('a','')

#문자열 색인(추출)
'abcde'[0:3]

#문자열 삽입 pad
s1 = Series(['abc','def'])
s1.str.pad(5, 'left','^')   #총자리수, 삽입할 방향, 삽입할 글자
#출력결과
#0    ^^abc
#1    ^^def
#dtype: object

#문자열 결합 cat
s4 = Series(['abc','def','123'])
print(s4.str.cat())
print(s4.str.cat(sep='/'))
#출력결과
#abcdef123
#abc/def/123

s5 = Series([['a','b','c'],
            ['d','e','f']])
print(s5.str.join(sep=''))
print(s5.str.join(sep='/'))
#출력결과
#0    abc
#1    def
#dtype: object
#0    a/b/c
#1    d/e/f
#dtype: object
```



**이메일 아이디 추출하기**

```python
s3 = Series(['abc@abc.com', 'leesh@rulru.com'])
#1
s3.map(lambda x: x[:x.find('@')])
#2
vno=s3.str.find('@')
list(map(lambda x,y: x[0:y], s3, vno))
```

 

---

### DataFrame

