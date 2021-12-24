# .CSV

> 데이터를 가지고 전처리 과정을 거친 후 원하는 결과물 출력
>
> (csv는 이 과정에서 데이터)



→ [기상자료개방포털 사이트](https://data.kma.go.kr/cmmn/main.do)에서 기온분석 데이터 가져오기

→ 저장 시 파일 형식은 CSV(쉼표로 분리)(*.csv)로 설정



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
3. f를 reader()함수에 넣어 data라는 csv reader 객체 생성
4. data 출력
5. 2번에서 연 파일 닫기



