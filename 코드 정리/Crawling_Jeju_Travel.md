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

```python
jeju_eating_list_df = pd.DataFrame(jeju_eating_list)
jeju_eating_list_df.columns = ['장소이름', '경도','위도','검색어']
jeju_eating_list_df
jeju_enjoy_list_df = pd.DataFrame(jeju_enjoy_list)
jeju_enjoy_list_df.columns = ['장소이름', '경도','위도','검색어']
jeju_nature_list_df = pd.DataFrame(jeju_nature_list)
jeju_nature_list_df.columns = ['장소이름', '경도','위도','검색어']
```

```python
#지도에 그려보기
import folium
from folium.plugins import MarkerCluster
locations = []
names = []

for i in range(len(jeju_total_df)):
    data = jeju_total_df.iloc[i]
    locations.append((float(data['위도']), float(data['경도'])))
    names.append(data['장소이름'])
    
#print(locations)

Mt_Hanla = [33.362500,126.533694]
map_jeju2 = folium.Map(location = Mt_Hanla,
                     zoom_start = 11)
#https://deparkes.co.uk/2016/06/10/folium-map-tiles/
tiles = ['stamenwatercolor', 'cartodbpositron', 
         'openstreetmap', 'stamenterrain','cartodbdark_matter']

for tile in tiles:
    folium.TileLayer(tile).add_to(map_jeju2)
    
marker_cluster = MarkerCluster(locations = locations,
                             popups = names,
                             name = 'jeju',
                             overlay = True,
                             control = True).add_to(map_jeju2)

folium.LayerControl().add_to(map_jeju2)
map_jeju2
```

```python
import folium
from folium.plugins import MarkerCluster
import json
import pandas as pd
from pandas.io.json import json_normalize
import os
locations_lat_eating = []
locations_lng_eating = []
names = []
locations_lat_enjoy = []
locations_lng_enjoy = []

locations_lat_nature = []
locations_lng_nature = []

for i in range(len(jeju_total_df)):       #총 개수만큼 돌아가
    data = jeju_total_df.iloc[i]
    names.append(data['장소이름'])         #name리스트에 장소이름 추가해
    

for i in range(len(jeju_eating_list_df)):       #총 개수만큼 돌아가
    data = jeju_eating_list_df.iloc[i]          #행 돌아가면서 data에 들어가
    locations_lat_eating.append(float(data['위도']))  #locations에 위도를 float형태로 넣어
    locations_lng_eating.append(float(data['경도']))
    
for i in range(len(jeju_enjoy_list_df)):       #총 개수만큼 돌아가
    data = jeju_enjoy_list_df.iloc[i]          #행 돌아가면서 data에 들어가
    locations_lat_enjoy.append(float(data['위도']))  #locations에 위도를 float형태로 넣어
    locations_lng_enjoy.append(float(data['경도']))
    
for i in range(len(jeju_nature_list_df)):       #총 개수만큼 돌아가
    data = jeju_nature_list_df.iloc[i]          #행 돌아가면서 data에 들어가
    locations_lat_nature.append(float(data['위도']))  #locations에 위도를 float형태로 넣어
    locations_lng_nature.append(float(data['경도']))
    
    
Mt_Hanla = [33.362500,126.533694]
map_jeju2 = folium.Map(location = Mt_Hanla,
                     zoom_start = 11)

#https://deparkes.co.uk/2016/06/10/folium-map-tiles/
tiles = ['stamenwatercolor', 'cartodbpositron', 
         'openstreetmap', 'stamenterrain','cartodbdark_matter']

for tile in tiles:
    folium.TileLayer(tile).add_to(map_jeju2)
    
for i in range(len(locations_lat_eating)):
    latitude = locations_lat_eating[i]
    longitude = locations_lng_eating[i]
    folium.Marker(location = [latitude,longitude],
                 #popup = ,
                 tooltip = '<pre>' + names[i] + '</pre>',
                 icon = folium.Icon(color = 'orange',
                                    #icon_color = 'red',
                                    #icon = 'info-sign',
                                    #icon = '',
                                    prefix = 'fa')).add_to(map_jeju2)
for i in range(len(locations_lat_enjoy)):
    latitude = locations_lat_enjoy[i]
    longitude = locations_lng_enjoy[i]
    folium.Marker(location = [latitude,longitude],
                 #popup = ,
                 tooltip = '<pre>' + names[i] + '</pre>',
                 icon = folium.Icon(color = 'lightblue',
                                    #icon_color = 'blue',
                                    #icon = 'info-sign',
                                    #icon = 'wifi',
                                    prefix = 'fa')).add_to(map_jeju2)
    
for i in range(len(locations_lat_nature)):
    latitude = locations_lat_nature[i]
    longitude = locations_lng_nature[i]
    folium.Marker(location = [latitude,longitude],
                 #popup = ,
                 tooltip = '<pre>' + names[i] + '</pre>',
                 icon = folium.Icon(color = 'green',
                                    #icon_color = '',
                                    #icon = 'info-sign',
                                    #icon = 'wifi',
                                    prefix = 'fa')).add_to(map_jeju2)



folium.LayerControl().add_to(map_jeju2)
map_jeju2
```

