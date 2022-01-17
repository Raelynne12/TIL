# 인스타그램 크롤링(가장 뜨는 제주도 맛집은 어딜까?)

> 인스타그램을 크롤링해서 제주도맛집 정보를 가져온 후
>
> 해시태그별 언급수 등을 파악하고 barplot과 wordcloud로 나타내기



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
```

```python
service = Service('../chromedriver.exe')
driver = webdriver.Chrome(service = service)
url = 'https://www.instagram.com'
driver.get(url)
time.sleep(3)
```

```python
#검색할 태그써서 경로찾는 함수
def insta_searching(word):
    url = 'https://www/instagram.com/explore/tags/' + word  #이렇게 써도 됨
    return url  #이 함수를 호출하면 url이 나오게
```

```python
#제주도맛집이라고 치고 한 번 해보기
word  = '제주도맛집'
driver.get(insta_searching(word))
time.sleep(5)
```

```python
from selenium.webdriver.common.bt import By

#여러 게시물들 중 첫 번째 게시물 클릭하게 하는 함수
def select_first(driver):
    first = driver.find_element(By.CSS_SELECTOR, 'div_9AhH0') #html 안에서 움직이게 도와줌
    first.click()
    time.sleep(3)
select_first(driver)
```

```python
#데리고 올 내용 : 본문 내용, 해시태그, 작성일자, 좋아요수, 위치정보
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#본문 내용
content = soup.select('div.C4VMK > span')[0].text 
content  #하면 본문 내용 나옴

#해시태그
import re
tags = re.findall(r'#\w+', content) #본문 내용에서 하나 이상되는 문자들 뽑아라#
tags = re.findall(r'#[^\s#,\\]+', content) #위에 + ^\/이런 거 없으면 나오게 하는
tags #하면 해시태그들 나옴

#작성일자
date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10] #데이트타임 속 10전까지
date #하면 작성일자 나옴

#좋아요수
like = soup.select('a.zV_Nj > span')[0].text
like #하면 좋아요수 나옴

#위치정보
place = soup.select('div > a.O4GIU')[0].text
place #하면 위치정보 나옴
```

```python
#위의 해본 내용들을 함수에 넣어보기
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    try:  #시도해봐라
        content = soup.select('div.C4VMK > span')[0].text
    except:  #만약 본문내용이 없으면
        content = '' #빈칸
    try:
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    except: #만약 작성일자가 없으면
        date = ''

    tags = re.findall(r'#[^\s#,\\]+', content) 
    
    try:
        like = soup.select('a.zV_Nj > span')[0].text
    except:  #만약 좋아요수가 나타나지 않으면
        like = 0
    try : 
        place = soup.select('div > a.O4GIU')[0].text
    except:  #만약 장소가 안쓰여있으면
        place = ''
    
    data = [content, date, like, place, tags]
    return(data)
```

