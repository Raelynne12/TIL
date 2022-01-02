# 날짜표현

> 월별, 일별, 요일별 집계
>
> 현재 날짜 - 입사일자 = 근무일자



### 현재 날짜

```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from datetime import datetime
d1 = datetime.now()		#지금 현재 시간
d1.year					#년도
d1.month				#달
d1.day					#일
```



### 날짜를 파싱

```
d2 = '2022/01/01'

```

