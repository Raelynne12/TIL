# pickle

> 데이터를 저장하고 불러올 때 매우 유용한 라이브러리
>
> 클래스 자체를 통째로 파일로 저장했다가 그대로 불러오기 가능
>
> 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장



**pickle로 저장하고 읽기**

````python
import pandas as pd
import pickle
temp = pd.DataFrame({'a':[1], 'b':[2]})
temp.to_pickle('./iampickle.pkl')
pd.read_pickle('./iampickle.pkl')
````



---

# openpyxl / bs4 / workbook 이용한 데이터 전처리

> 사용하기 위해서는 cmd 창이나 주피터 노트북 또는 구글 코랩에 아래와 같이 써서 다운로드 받아야 한다.
>
> pip install openpyxl
>
> pip install bs4
>
> pip install Workbook



**약국 정보 리스트 가져와서 필요한 정보만 전처리**

```python
#약국 정보 서비스 API
#https://www.data.go.kr/iim/api/selectAPIAcountView.do

api = https://www.data.go.kr/iim/api/selectAPIAcountView.do
apikey = #본인 apikey 입력

import pandas as pd
import numpy as np
import requests								#네트워크에서 요청
from openpyxl.workbook import Workbook		#파이썬 엑셀 파일로 나오게
from bs4 import BeautifulSoup				#파이썬 라이브러리, 정적인 데이터 때 사용

list_drugs = ['병원명', '종별코드명', '시도명', '주소', '전화번호']

for list_drug in list_drugs:
	url = api.format(list_drugs, key = apikey)
	req = requests.get(url)
	re = req.text
	soup = BeautifulSoup(re, 'html.parser')
	#병원명
	yadmnm = soup.find_all('yadmnm')
	#종별코드명
	sggucdnm = soup.find_all('sggucdnm')
	#시도명
	sidocdnm = soup.find_all('sidocdnm')
	#주소
	addr = soup.find_all('addr')
	#전화번호
	telno = soup.find_all('telno')

print('병원명', yadmnm)
print('종별코드명', sggucdnm)
print('시도명', sidocdnm)
print('주소', addr)
print('전화번호', telno)
```

```python
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
#https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8
html = requests.get("https://search.naver.com/search.naver?query=날씨")
print(html)

html = requests.get('https://weather.naver.com/today')
soup = bs(html.text, 'html.parser')
print(soup)
#미세먼지 데이터 가져오기

dustdata_one = soup.find('ul', {'class' : 'today_chart_list'})
print(dustdata_one)

dustdata_all[0].find('em', {'class' : 'level_text'}).text
#출력결과
#'좋음'
```

