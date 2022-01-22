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

