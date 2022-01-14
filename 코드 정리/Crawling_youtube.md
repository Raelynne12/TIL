# 유튜브 차트 top 100 크롤링해서 엑셀파일로 저장하기

> [카테고리 / 가수명 / 구독자수 / view수 / 동영상수] << 리스트



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
```

```python
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'
service = Service('../chromedriver.exe')
driver = webdriver.Chrome(service = service)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
```

```python
genres = soup.select('tbody > tr')
len(genres)				#101
genres = genres[:-1]	#슬라이싱해서 100으로
genre = genres[0]

#카테고리
category = genre.select('p.category')[0].text.strip()
#가수명
name = genre.select('td > h1 > a')[0].text.strip()
#구독자수
sub = genre.select('td.subscriber_cnt')[0].text
#view수
view = genre.select('td.view_cnt')[0].text
#동영상수
video = genre.select('td.video_cnt')[0].text
```

```python
yotubers = []

for genre in genres:
    category = genre.select('p.category')[0].text.strip()
    name = genre.select('td > h1 > a')[0].text.strip()
    sub = genre.select('td.subscriber_cnt')[0].text
    view = genre.select('td.view_cnt')[0].text
    video = genre.select('td.video_cnt')[0].text
    mylist = [category, name, sub, view, video]
    youtubers.append(mylist)
    
columns = ['카테고리','가수명','구독자수','view수','동영상수']
df_youtubers = pd.DataFrame(youtubers, columns = columns)	#DataFrame으로 만들어줘야 엑셀ㅇ
df_yotubers.to_excel('./files/youtube_rank_class.xlsx')
```

