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

