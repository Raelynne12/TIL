# 배운 내용들로 우리 가족 제주도 여행 위한 제주도 여행 데이터 크롤링 후 시각화

> 크롬드라이버로 인스타 설정 후
>
> searching 함수로 url 들어가고
>
> 내용/날짜/태그/좋아요수/장소 
>
> 다음장으로 넘어가는 함수
>
> 데이터 프레임으로
>
> 엑셀로 저장



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
service = Service('../chromedriver.exe')
driver = webdriver.Chrome(service = service)
```

```python
#크롬드라이버로 인스타 설정
def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url
```

```python
#첫번째 인기게시물 클릭
from selenium.webdriver.common.by import By
def select_first(driver):
    first = driver.find_element(By.CSS_SELECTOR, 'div._9AhH0')
    first.click()
    time.sleep(2)
```

```python
#content, tags, date, like, place
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

content = soup.select('div.C4VMK > span')[0].text

import re
tags = re.findall(r'#[^\s#,\\]+', content)

date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

like = soup.select('a.zV_Nj > span')[0].text

place = soup.select('div > a.O4GlU')[0].text
```

```python
#위의 것들을 함수로
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    try:
        content = soup.select('div.C4VMK > span')[0].text
    except:
        content = ''
    try:
        tags = re.findall(r'#[^\s#,\\]+', content)
    except:
        tags = 0
    try:
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    except:
        date = ''
    try:
        like = soup.select('a.zV_Nj > span')[0].text
    except:
        like = 0
    try:
        place = soup.select('div > a.O4GlU')[0].text
    except:
        place = ''
        
    data = [content, date, like, place, tags]
    return(data)
```

```python
#다음 장으로 넘겨주기
#from selenium.webdriver.common.by import By

def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR, 'div.l8mY4.feth3')
    right.click()
    time.sleep(3)

move_next(driver)
```

```python
#메인
from tqdm.notebook import tqdm
def insta_crawling(word, n):
    url = insta_searching(word)
    
    driver.get(url)
    time.sleep(5)
    
    select_first(driver)
    time.sleep(3)
    
    results = []
    
    for i in tqdm(range(n)):
        try:
            data = get_content(driver)
            results.append(data)
            move_next(driver)
            
        except:
            time.sleep(2)
            move_next(driver)
            
    return(results)
```

```python
#제주도 여행으로 검색하기
travel_place = insta_crawling('제주도여행', 200)
```

```python
travel_place_df = pd.DataFrame(travel_place)
travel_place_df.columns = ['contents', 'date','like','place','tags']
travel_place_df
```

```python
travel_place_df.drop_duplicates(subset = ['contents'],inplace = True)
travel_place_df.shape   #65개 없어짐 >> (188,5)
#travel_place_df.head()
```

```
```

