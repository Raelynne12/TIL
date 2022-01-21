# 롯데 on 사이트에서 베이스메이크업 리스트 뽑기

> 백화점 쇼핑몰 페이지에 있는 베이스메이크업 인기 제품들의 소스들을 크롤링 후 
>
> 엑셀파일로 저장하고 시각화하기



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import folium
import json
```

