## 크롤링으로 멜론차트 top 100 엑셀파일 만들기

> 크롤링으로 멜론차트 데이터 가져오고 
>
> 엑셀파일로 저장하기

```python
from selenium import webdriver
from selenim.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame

url = 'https://www.melon.com/chart/index.htm'
service = Service('../chromedriver.exe')
driver = webdriver.Chrome(service = service)	#앞 service는 변수 이름 뒤 service는 위에 service
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
soup
```

```python
songs = soup.select('tbody > tr')
song = songs[0]
title = song.select('div.ellipsis.rank01 > span > a')[0].text
name = song.select('div.ellipsis.rank02 > a')[0].text
rank = 1

chart = []

for song in songs:
    title = song.select('div.ellipsis.rank01 > span > a')[0].text
    name = song.select('div.ellipsis.rank02 > a')[0].text
    mylist = ['melon', rank, title, name]
    chart.append(mylist)
    rank += 1
    
columns = ['서비스', '순위', '타이틀','가수']
df_chart = pd.DataFrame(chart, columns = columns)
df_chart.to_excel('./files/melon_class.xlsx',
                 sheet_name = 'melon top 100')
```



---

## 벅스 top 100 엑셀파일

```python
service = Service('../chromedriver/exe')
driver = webdriver.Chrome(service = service)
url = 'https://music.bugs.co.kr/chart/'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('tbody > tr')
songs = songs[:-3]		#len(songs)가 103이 나와서 슬라이싱(top 100으로 만들기 위해)
song = songs[0]	
#슬라이싱 대신에
#songs = soup.select('table.byChart > tbody > tr') 이렇게 해도 됨
title = song.select('p.title > a')[0].text
name = song.select('p.artist > a')[0].text
rank = song.select('td > div.ranking > strong')[0].text

chart = []

for song in songs:
    title = song.select('p.title > a')[0].text
    name = song.select('p.artist > a')[0].text
    rank = song.select('td > div.ranking > strong')[0].text
    mylist = ['bugs', rank, title, name]
    chart.append(mylist)
    
columns = ['서비스', '순위', '타이틀', '가수']
df_chart = pd.DataFrame(chart, columns = columns)
df_chart.to_excel('./files/bugs_class.xlsx',
                 sheet_name = 'bugs top 100')
```



---

## 지니 top 50 엑셀파일

```python
service = service('../charomedriver.exe')
driver = webdriver.Chrome(service = service)
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song = songs[0]
title = song.select('td > a.title.ellipsis')[0].text.strip()	#쓸데없는 빈공간이 많아서 strip()
name = song.select('td > a.artist.ellipsis')[0].text

chart = []
rank = 1

for song in songs:
    title = song.select('td > a.title.ellipsis')[0].text.strip()
    name = song.select('td > a.artist.ellipsis')[0].text
    mylist = ['genie', rank, title, name]
    chart.append(mylist)
    rank += 1
   
columns = ['서비스', '순위', '타이틀', '가수']
df_chart = pd.DataFrame(chart, columns = columns)
df_chart.to_Excel('./files/genie_class.xlsx',
                 sheet_name = 'genie top 50')
```

