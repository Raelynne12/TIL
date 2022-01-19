# 왜 우리 동네에는 스타벅스가 없을까?

> 서울에서 스타벅스가 어떤 전략으로 매장입지를 선택하는지 살펴보기
>
> \> 스타벅스의 매장 입지에 대한 두 가지 가설을 세우고, 맞는지 데이터 분석을 통해 알아보기
>
> \>> 1. 거주 인구가 많은 지역에 스타벅스 매장이 많이 입지해 있을 것이다
>
> \>> 2. 직장인이 많은 지역에 스타벅스 매장이 많이 입지해 있을 것이다
>
> 이를 위해 스타벅스 위치를 파악하고, 인구통계 데이터 수집해야



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time
```

```python
# (1) 서울시 어떤 군구가 스타벅스가 많니
service = Service('../chromedriver.exe')
driver = webdriver.Chrome(service = service)
url = 'https://www.starbucks.co.kr/store/store_map.do'
driver.get(url)
```

```python
#지역검색 클릭하게
find_geography = '#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a'
driver.find_element(By.CSS_SELECTOR, find_geography).click()

#서울 지역 클릭하게
seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
driver.find_element(By.CSS_SELECTOR, seoul_btn).click()
time.sleep(3)

#서울 전체 지역 클릭하게
all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
driver.find_element(By.CSS_SELECTOR, all_btn).click()
time.sleep(3)
```

```python
#568개 서울시 크롤링
#이름, 위도, 경도, 가게타입, 주소, 전화번호
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

starbucks_soup_list = soup.select('div.loca_step3 li.quickResultLstCon')
len(starbucks_soup_list)   #568 얘가 서울 전체 지역 스타벅스 

starbucks_store = starbucks_soup_list[0] #첫 번째 애 데려와
starbucks_store

name = starbucks_store.select('strong')[0].text.strip() #태그 접근할 때()
lat = starbucks_store['data-lat'].strip() #데이터 접근할 때 []
lng = starbucks_store['data-long'].strip()
store_type = starbucks_store.select('i')[0]['class'][0][4:].strip()
address = starbucks_store('p')[0].text[:-9]
tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
```

```python
#568개 데이터 가져오기 리스트로
starbucks_list = []

for starbucks_store in starbucks_soup_list:
    name = starbucks_store.select('strong')[0].text.strip() #태그 접근할 때()
    lat = starbucks_store['data-lat'].strip() #데이터 접근할 때 []
    lng = starbucks_store['data-long'].strip()
    store_type = starbucks_store.select('i')[0]['class'][0][4:].strip()
    address = starbucks_store('p')[0].text[:-9]
    tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
    
    mylist = [name, lat, lng, store_type, address, tel]
    starbucks_list.append(mylist)

#리스트를 데이터프레임(표) 형태로 저장(컬럼이름도 변경)
columns = ['매장명','위도','경도','매장타입','주소','전화번호']
seoul_starbucks_df = pd.DataFrame(starbucks_list,
                                 columns = columns)
seoul_starbucks_df.head()
```

![image-20220119223026495](Crawling_Starbucks.assets/image-20220119223026495.png)

```python
#엑셀파일로 저장
seoul_starbucks_df.to_excel('./files/seoul_starbucks_list_mine.xlsx', index = False)
```



---

```python
#(2) 시군구마다의 인구
#서울시 열린인구 데이터 ~ 에서 api가져오기
import requests
```

```python
SEOUL_API_AUTH_KEY = #자기 api키
Open_API = 'GangseoListLoanCompany'
url =  'http://openAPI.seoul.go.kr:8088/{}/json/{}/1/5/'.format(SEOUL_API_AUTH_KEY, Open_API)
```

```python
result_dict = requests.get(url).json()
result_dict #list_total_count >> 데이터 전체 개수 / code >> inf0-000나오는거면 정상
result_dict['GangseoListLoanCompany']['list_total_count'] #접근방식은 이런 식
```

```python
sample_df = pd.DataFrame(result_dict['GangseoListLoanCompany']['row'])
sample_df
```

![image-20220119232234501](Crawling_Starbucks.assets/image-20220119232234501.png)

```python
#서울시 주민등록 인구 자료 불러옴
sgg_pop_df = pd.read_csv('../6_Starbucks_Location/files/report.txt',
                        header = 2, sep = '\t')
sgg_pop_df.head()
```

![image-20220119232211661](Crawling_Starbucks.assets/image-20220119232211661.png)



```python
url = 'http://openAPI.seoul.go.kr:8088/{}/json/{}/1/5/'.format(Open_API, service)
service = 'GangseoListLoanCompany'

def seoul_open_api_data(url, service):
    data_list = None
    try:
        result_dict = requests.get(url).json()
        result_data = result_dict[service]
        code = result_data['RESULT']['CODE']
        
        if code == 'INF0-000':
            data_list = result_data['row']
    except:
        pass
    return(data_list)
seoul_open_api_data(url, service)
```

```
```

