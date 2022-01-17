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

```
```

