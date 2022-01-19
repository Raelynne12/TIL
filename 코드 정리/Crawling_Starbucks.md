# 왜 우리 동네에는 스타벅스가 없을까?



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