# 배운 내용들을 가지고 제주 가족여행 지도 만들기

> 우선적으로 가기로 했던 장소들을 지도에 매핑하고
>
> 주제별로 구분(맛집, 오름, 카페 등)
>
> 이외에 더 갈 곳이나 유명한 곳들은 인스타그램에서 크롤링해서 정보 얻은 후 매핑



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
```

```python
#위도경도 (x,y)찾기
def find_places(searching):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
          'Authorization':'KakaoAK 자기 api키'
    }
    places = requests.get(url, headers = headers).json()['documents']
    place = places[0]
    name = place['place_name']
    x = place['x']
    y = place['y']
    
    data = [name , x, y, searching]
    
    return(data)
```

```python
#함수에 넣을 리스트 만들기
locations_nature = ['통일전망대','산굼부리','섭지코지','성산일출봉']
locations_eating = ['제주이와이']
locations_enjoy = ['노형수퍼마켙']

jeju_nature_list = []
jeju_eating_list = []
jeju_enjoy_list = []

#자연경관 리스트
for location in locations_nature:
    lo = find_places(location)
    mylist = [lo]
    jeju_nature_list.append(mylist)
jeju_nature_list

#맛집 리스트
for location in locations_eating:
    lo = find_places(location)
    mylist_eating = [lo]
    jeju_eating_list.append(mylist_eating)
jeju_eating_list

#즐길거리 리스트
for location in locations_enjoy:
    lo = find_places(location)
    mylist_enjoy = [lo]
    jeju_enjoy_list.append(mylist_enjoy)
jeju_enjoy_list
```

