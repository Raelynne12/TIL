```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import time
import itertools
import gc
import pickle
from datetime import datetime
#from xgboost import XGBRegressor
#from xgboost import plot_importance

%matplotlib inline
```


```python
# 데이터 불러오기
sales = pd.read_csv('sales_train.csv')
items = pd.read_csv('items.csv')
item_categories = pd.read_csv('item_categories.csv')
shops = pd.read_csv('shops.csv')
test = pd.read_csv('test.csv')
```

# 1. 전처리

## 2. sales 데이터


```python
sales.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>date_block_num</th>
      <th>shop_id</th>
      <th>item_id</th>
      <th>item_price</th>
      <th>item_cnt_day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>02.01.2013</td>
      <td>0</td>
      <td>59</td>
      <td>22154</td>
      <td>999.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>03.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2552</td>
      <td>899.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2552</td>
      <td>899.00</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2554</td>
      <td>1709.05</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2555</td>
      <td>1099.00</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
sales.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2935849 entries, 0 to 2935848
    Data columns (total 6 columns):
     #   Column          Dtype  
    ---  ------          -----  
     0   date            object 
     1   date_block_num  int64  
     2   shop_id         int64  
     3   item_id         int64  
     4   item_price      float64
     5   item_cnt_day    float64
    dtypes: float64(2), int64(3), object(1)
    memory usage: 134.4+ MB
    


```python
sales = sales.date.apply(lambda x : datetime.strptime(x,'%d.%m.%Y'))
sales
```




    0         2013-01-02
    1         2013-01-03
    2         2013-01-05
    3         2013-01-06
    4         2013-01-15
                 ...    
    2935844   2015-10-10
    2935845   2015-10-09
    2935846   2015-10-14
    2935847   2015-10-22
    2935848   2015-10-03
    Name: date, Length: 2935849, dtype: datetime64[ns]




```python
sales.shape # (2935849, 6)
```




    (2935849, 6)




```python
sales.corr()  # 상관계수
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_block_num</th>
      <th>shop_id</th>
      <th>item_id</th>
      <th>item_price</th>
      <th>item_cnt_day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>date_block_num</th>
      <td>1.000000</td>
      <td>0.019273</td>
      <td>0.009356</td>
      <td>0.095010</td>
      <td>0.009402</td>
    </tr>
    <tr>
      <th>shop_id</th>
      <td>0.019273</td>
      <td>1.000000</td>
      <td>0.029396</td>
      <td>-0.024034</td>
      <td>-0.005230</td>
    </tr>
    <tr>
      <th>item_id</th>
      <td>0.009356</td>
      <td>0.029396</td>
      <td>1.000000</td>
      <td>-0.134104</td>
      <td>0.016650</td>
    </tr>
    <tr>
      <th>item_price</th>
      <td>0.095010</td>
      <td>-0.024034</td>
      <td>-0.134104</td>
      <td>1.000000</td>
      <td>0.011197</td>
    </tr>
    <tr>
      <th>item_cnt_day</th>
      <td>0.009402</td>
      <td>-0.005230</td>
      <td>0.016650</td>
      <td>0.011197</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
sales.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_block_num</th>
      <th>shop_id</th>
      <th>item_id</th>
      <th>item_price</th>
      <th>item_cnt_day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.935849e+06</td>
      <td>2.935849e+06</td>
      <td>2.935849e+06</td>
      <td>2.935849e+06</td>
      <td>2.935849e+06</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.456991e+01</td>
      <td>3.300173e+01</td>
      <td>1.019723e+04</td>
      <td>8.908532e+02</td>
      <td>1.242641e+00</td>
    </tr>
    <tr>
      <th>std</th>
      <td>9.422988e+00</td>
      <td>1.622697e+01</td>
      <td>6.324297e+03</td>
      <td>1.729800e+03</td>
      <td>2.618834e+00</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>-1.000000e+00</td>
      <td>-2.200000e+01</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.000000e+00</td>
      <td>2.200000e+01</td>
      <td>4.476000e+03</td>
      <td>2.490000e+02</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.400000e+01</td>
      <td>3.100000e+01</td>
      <td>9.343000e+03</td>
      <td>3.990000e+02</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.300000e+01</td>
      <td>4.700000e+01</td>
      <td>1.568400e+04</td>
      <td>9.990000e+02</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.300000e+01</td>
      <td>5.900000e+01</td>
      <td>2.216900e+04</td>
      <td>3.079800e+05</td>
      <td>2.169000e+03</td>
    </tr>
  </tbody>
</table>
</div>



- 중복데이터 처리


```python
sales = sales.drop_duplicates()
sales.shape  # (2935849, 6) -> (2935843, 6)
```




    (2935843, 6)



- 특정 행 제거


```python
# item_price 가 0 이하인 경우
(sales.item_price <= 0).sum()
```




    1




```python
sales = sales[sales.item_price > 0]
```


```python
# 팔린 상품의 개수가 (-) 인 경우 -> 행 삭제?, 이전 주문과 함께 삭제
(sales['item_cnt_day'] < 0).sum()
```




    7356




```python
sales = sales[sales.item_cnt_day >= 0]
```

- 결측치 처리


```python
# 결측치 없음
sales.isnull().sum()
```




    date              0
    date_block_num    0
    shop_id           0
    item_id           0
    item_price        0
    item_cnt_day      0
    dtype: int64



- 이상치 처리


```python
plt.figure(figsize=(12,3))
sns.boxplot(x='item_price', data=sales)
plt.figure(figsize=(12,3))
sns.boxplot(x='item_cnt_day', data=sales)
plt.show()
```


    
![png](output_20_0.png)
    



    
![png](output_20_1.png)
    



```python
plt.figure(figsize=(12,3))
sns.boxplot(x = 'date_block_num', y = 'item_price', data = sales)
plt.figure(figsize=(12,3))
sns.boxplot(x = 'date_block_num', y = 'item_cnt_day', data = sales)
plt.show()
```


    
![png](output_21_0.png)
    



    
![png](output_21_1.png)
    



```python
# 뚜렷한 이상치를 우선 제거 -> 분석하면서 확인하기
sales = sales[sales.item_cnt_day < 500]
sales = sales[sales.item_price < 50000]
```


```python
plt.figure(figsize=(12,3))
sns.boxplot(x='item_price', data=sales);
plt.figure(figsize=(12,3))
sns.boxplot(x='item_cnt_day', data=sales)

plt.show()
```


    
![png](output_23_0.png)
    



    
![png](output_23_1.png)
    


## 2. items data


```python
items
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_name</th>
      <th>item_id</th>
      <th>item_category_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>! ВО ВЛАСТИ НАВАЖДЕНИЯ (ПЛАСТ.)         D</td>
      <td>0</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>!ABBYY FineReader 12 Professional Edition Full...</td>
      <td>1</td>
      <td>76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>***В ЛУЧАХ СЛАВЫ   (UNV)                    D</td>
      <td>2</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>***ГОЛУБАЯ ВОЛНА  (Univ)                      D</td>
      <td>3</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>***КОРОБКА (СТЕКЛО)                       D</td>
      <td>4</td>
      <td>40</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>22165</th>
      <td>Ядерный титбит 2 [PC, Цифровая версия]</td>
      <td>22165</td>
      <td>31</td>
    </tr>
    <tr>
      <th>22166</th>
      <td>Язык запросов 1С:Предприятия  [Цифровая версия]</td>
      <td>22166</td>
      <td>54</td>
    </tr>
    <tr>
      <th>22167</th>
      <td>Язык запросов 1С:Предприятия 8 (+CD). Хрустале...</td>
      <td>22167</td>
      <td>49</td>
    </tr>
    <tr>
      <th>22168</th>
      <td>Яйцо для Little Inu</td>
      <td>22168</td>
      <td>62</td>
    </tr>
    <tr>
      <th>22169</th>
      <td>Яйцо дракона (Игра престолов)</td>
      <td>22169</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
<p>22170 rows × 3 columns</p>
</div>




```python
items.drop(['item_name'], axis=1, inplace=True)
```


```python
items.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_id</th>
      <th>item_category_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>



### 3. item_categoris data


```python
item_categories.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_category_name</th>
      <th>item_category_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PC - Гарнитуры/Наушники</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Аксессуары - PS2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Аксессуары - PS3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Аксессуары - PS4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Аксессуары - PSP</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
type_encoder = LabelEncoder()
item_categories['split_name'] = item_categories['item_category_name'].str.split(' - ')
item_categories['type'] = item_categories['split_name'].map(lambda x: x[0].strip())
item_categories['type_id'] = type_encoder.fit_transform(item_categories['type'])
```


```python
item_categories.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_category_name</th>
      <th>item_category_id</th>
      <th>split_name</th>
      <th>type</th>
      <th>type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PC - Гарнитуры/Наушники</td>
      <td>0</td>
      <td>[PC, Гарнитуры/Наушники]</td>
      <td>PC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Аксессуары - PS2</td>
      <td>1</td>
      <td>[Аксессуары, PS2]</td>
      <td>Аксессуары</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Аксессуары - PS3</td>
      <td>2</td>
      <td>[Аксессуары, PS3]</td>
      <td>Аксессуары</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Аксессуары - PS4</td>
      <td>3</td>
      <td>[Аксессуары, PS4]</td>
      <td>Аксессуары</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Аксессуары - PSP</td>
      <td>4</td>
      <td>[Аксессуары, PSP]</td>
      <td>Аксессуары</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
item_categories = item_categories[['item_category_id','type_id']]
```


```python
item_categories.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_category_id</th>
      <th>type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### 4. shops data


```python
shops.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>shop_name</th>
      <th>shop_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>!Якутск Орджоникидзе, 56 фран</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>!Якутск ТЦ "Центральный" фран</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Адыгея ТЦ "Мега"</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Балашиха ТРК "Октябрь-Киномир"</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Волжский ТЦ "Волга Молл"</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
shops.loc[shops.shop_name == 'Сергиев Посад ТЦ "7Я"', 'shop_name'] = 'СергиевПосад ТЦ "7Я"'
```


```python
# 공백(' ')을 기준으로 분리
shops['city'] = shops['shop_name'].str.split(' ').map(lambda x: x[0])
```


```python
shops.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>shop_name</th>
      <th>shop_id</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>!Якутск Орджоникидзе, 56 фран</td>
      <td>0</td>
      <td>!Якутск</td>
    </tr>
    <tr>
      <th>1</th>
      <td>!Якутск ТЦ "Центральный" фран</td>
      <td>1</td>
      <td>!Якутск</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Адыгея ТЦ "Мега"</td>
      <td>2</td>
      <td>Адыгея</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Балашиха ТРК "Октябрь-Киномир"</td>
      <td>3</td>
      <td>Балашиха</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Волжский ТЦ "Волга Молл"</td>
      <td>4</td>
      <td>Волжский</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_encoder = LabelEncoder()
shops['city_id'] = city_encoder.fit_transform(shops['city'])
shops = shops[['shop_id', 'city_id']]
shops.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>shop_id</th>
      <th>city_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
shops.city_id.value_counts()
```




    14    13
    25     3
    5      3
    19     3
    0      2
    12     2
    30     2
    26     2
    21     2
    20     2
    17     2
    16     2
    9      2
    7      2
    11     1
    23     1
    2      1
    29     1
    28     1
    27     1
    3      1
    4      1
    24     1
    22     1
    13     1
    6      1
    8      1
    18     1
    1      1
    15     1
    10     1
    31     1
    Name: city_id, dtype: int64



### 5. test data


```python
test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>shop_id</th>
      <th>item_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>5</td>
      <td>5037</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>5</td>
      <td>5320</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5</td>
      <td>5233</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
      <td>5232</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>5268</td>
    </tr>
  </tbody>
</table>
</div>




```python
test.shape
```




    (214200, 3)




```python
# test 데이터에서 shop_id는 42개 >> 상점수가 42개래
len(test.shop_id.unique())
```




    42




```python
# test 데이터에는 있지만 sales 데이터에는 없는 item_id가 총 363개 있다.
# 363개의 item_id에 대한 판매량은 0으로 예측
len(set(test.item_id) - set(sales.item_id))
```




    363




```python

```


```python
### 환불 적용 모듈
train_F = sales.copy()
k = train_F[train_F.item_cnt_day < 0]
qwe = 0
minimum = 0
timefunc = time.time()
for i in range(len(k)):
    try:
        if k.iloc[i,5] < minimum:
            minimum = k.iloc[i,5]
        a = (train_F[np.array(train_F.item_id == k.iloc[i,3]) & np.array(train_F.shop_id == k.iloc[i,2])])
        if a.date.min() < k.iloc[i,0]:
            h = a[a.date==a.date[a.date < k.iloc[i,0]].max()].index[0]
            qwe += 1
            train_F.loc[h,'item_cnt_day'] += k.iloc[i,5]
#            if qwe == 5:
#                break
        else:
            pass
    except:
        pass
train_F.drop(k.index,axis = 0,inplace = True)
print(len(k))
print('필요 없는 값:',(len(k) - qwe))
print('적용한 값의 수::',qwe)
print(minimum)
print(time.time() - timefunc)
```

    0
    필요 없는 값: 0
    적용한 값의 수:: 0
    0
    0.8479084968566895
    


```python

```

### 데이터 merge


```python
sales['item_category_id']=items['item_category_id']
sales.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>date_block_num</th>
      <th>shop_id</th>
      <th>item_id</th>
      <th>item_price</th>
      <th>item_cnt_day</th>
      <th>item_category_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>02.01.2013</td>
      <td>0</td>
      <td>59</td>
      <td>22154</td>
      <td>999.00</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>03.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2552</td>
      <td>899.00</td>
      <td>1.0</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2554</td>
      <td>1709.05</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2555</td>
      <td>1099.00</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2564</td>
      <td>349.00</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python

```


```python

```

### 추가 컬럼 만들기


```python
sales.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>date_block_num</th>
      <th>shop_id</th>
      <th>item_id</th>
      <th>item_price</th>
      <th>item_cnt_day</th>
      <th>item_category_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>02.01.2013</td>
      <td>0</td>
      <td>59</td>
      <td>22154</td>
      <td>999.00</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>03.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2552</td>
      <td>899.00</td>
      <td>1.0</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2554</td>
      <td>1709.05</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2555</td>
      <td>1099.00</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2564</td>
      <td>349.00</td>
      <td>1.0</td>
      <td>40.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 총 수익
sales['revenue'] = sales['item_price'] * sales['item_cnt_day']
sales.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>date_block_num</th>
      <th>shop_id</th>
      <th>item_id</th>
      <th>item_price</th>
      <th>item_cnt_day</th>
      <th>item_category_id</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>02.01.2013</td>
      <td>0</td>
      <td>59</td>
      <td>22154</td>
      <td>999.00</td>
      <td>1.0</td>
      <td>40.0</td>
      <td>999.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>03.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2552</td>
      <td>899.00</td>
      <td>1.0</td>
      <td>76.0</td>
      <td>899.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2554</td>
      <td>1709.05</td>
      <td>1.0</td>
      <td>40.0</td>
      <td>1709.05</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2555</td>
      <td>1099.00</td>
      <td>1.0</td>
      <td>40.0</td>
      <td>1099.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10.01.2013</td>
      <td>0</td>
      <td>25</td>
      <td>2564</td>
      <td>349.00</td>
      <td>1.0</td>
      <td>40.0</td>
      <td>349.00</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

# 2. EDA

1. 월별 거래수


```python
#월별 거래수
sales.groupby('date_block_num').count()
sales.groupby('date_block_num')['date'].count()

transactions = sales.groupby('date_block_num')['date'].count()
transactions

plt.style.use('ggplot')
transactions.plot(title = 'number of transactions of month', color = 'black')
plt.show()

#전체적으로 월별 거래수가 꾸준히 하락함
#엄청 높게 치솟는 두 개 점은 연말(13년 12월, 14년 12월)임
```


    
![png](output_61_0.png)
    


2. 월별 거래된 shops 수, 월별 거래된 items 수


```python
#각 월 블록에서 매출 데이터에 거래가 있는 고유 상점 및 품목 수
shop_count = sales.groupby('date_block_num')['shop_id'].nunique()
item_count = sales.groupby('date_block_num')['item_id'].nunique()

sales.groupby('date_block_num').nunique()
#sales.groupby('date_block_num')['shop_id'].nunique() #월별 고유 상점수
#sales.groupby('date_block_num')['item_id'].nunique()  #d월별 고유 아이템수

sales['item_id'].nunique() #item 21802개
items['item_id'].nunique() #item 22170개
#sales['shop_id'].nunique() #shop 60개
shops['shop_id'].nunique() #shop 60개

#sales에 있는 item_id랑 items에 있는 item_id의 수가 다름
```




    60




```python
fig, ax = plt.subplots(1,2, figsize = (12,5))
shop_count.plot(ax = ax[0], color = 'red')
item_count.plot(ax = ax[1], color = 'blue')
ax[0].set_title('number of shops with transactions') #거래가 있는 상점수
ax[1].set_title('number of items with transactions') #거래된 아이템수
plt.show()
```


    
![png](output_64_0.png)
    



```python
#연말을 제외하고는 월별 거래수와 월별 거래된 아이템수 모두 하락세
#거래처들의 수는 2년차부터는 느는 듯 했으나 2말부터 훅훅 떨어짐

#그리고 거래처수가 60개로 나오는데 차트를 보면 매달 모든 가게에서 거래되는 게 아니고
#물건도 많이 못미친다
```

3. 상점 별 하루 item 판매 개수


```python
shop_ns = sales[['shop_id','item_cnt_day']]
shop_ns.set_index(['shop_id'])
shop_ns = shop_ns.groupby(by=['shop_id']).sum()
shop_ns.plot(kind = 'bar')
plt.show()
```


    
![png](output_67_0.png)
    


4. 가격 별 item 하루 판매 개수


```python
price_ns = sales[['item_price','item_cnt_day']]
price_ns = price_ns.groupby(by=['item_price']).sum()
plt.plot(price_ns.index, price_ns.values)
plt.xlabel('item_price')
plt.ylabel('item_cnt_day')
plt.show()
```


    
![png](output_69_0.png)
    


5. 월 별 총 판매금액


```python
# 월 별 총 판매금액
time_ns = sales[['item_price','date_block_num']]
time_ns = time_ns.groupby(by=['date_block_num']).sum()
plt.figure(figsize=(12,3))
plt.plot(time_ns.index, time_ns.values)
plt.show()
```


    
![png](output_71_0.png)
    


6. 월별 총 판매개수


```python
# 월 별 총 판매개수
group1 = sales.groupby(by=['date_block_num']).sum()
group1 = group1.reset_index()
plt.figure(figsize=(12,3))
plt.plot(group1.date_block_num,  group1.item_cnt_day)
plt.show()
```


    
![png](output_73_0.png)
    


7. 품목별 판매량


```python
# 품목별 판매량 
Category_sum=sales.groupby(['item_category_id'], as_index=False)['item_cnt_day'].sum()
fig, axes = plt.subplots(1,1,figsize = (35,8))
sns.barplot(x="item_category_id",y="item_cnt_day", data=Category_sum)
plt.show()
```


    
![png](output_75_0.png)
    



```python
# 카테고리별 판매금액
Category_sum=sales.groupby(['item_category_id'], as_index=False)['revenue'].sum()
fig, axes = plt.subplots(1,1,figsize = (35,8))
sns.barplot(x="item_category_id",y="revenue", data=Category_sum)
plt.show()
```


    
![png](output_76_0.png)
    



```python
#연도별 판매량  -> Year, Month 컬럼 만든 후 확인 가능합니다(이재호)
fig,axes = plt.subplots(1,1,figsize=(7,7))
sns.lineplot(x=sales_data['Year'],y=sales_data['item_cnt_day'])
plt.show()
```


```python
# 월별 판매량
fig,axes = plt.subplots(1,1,figsize=(7,7))
sns.lineplot(x=sales_data['Month'],y=sales_data['item_cnt_day'])
plt.show()
```


```python
# 연도별 판매총액 >> 14년 까진 꾸준하다가 14년부터 판매량 감소
fig,axes = plt.subplots(1,1,figsize=(7,7))
sns.lineplot(x=sales_data['Year'],y=sales_data['Sales_per_item'])
plt.show()
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python
# 상점별 월 item 판매개수 -> 월 별 item 판매개수 컬럼 만든 후 확인 가능합니다.(김홍비)
shop_ns = matrix[['shop_id','item_cnt_month']]
shop_ns.set_index(['shop_id'])
shop_ns = shop_ns.groupby(by=['shop_id']).sum()
shop_ns.plot(kind = 'bar')
plt.xlabel('shop_id')
plt.ylabel('item_cnt_month')
plt.show()
```


```python
# 카테고리별 판매개수
category_ns = matrix[['item_category_id','item_cnt_month']]
category_ns.set_index(['item_category_id'])
category_ns = category_ns.groupby(by=['item_category_id']).sum()
category_ns.plot(kind = 'bar')
plt.xlabel('category_id')
plt.ylabel('item_cnt_month')
plt.show()
```


```python
# 도시별 판매개수
city_ns = matrix[['city_id','item_cnt_month']]
city_ns.set_index(['city_id'])
city_ns = city_ns.groupby(by=['city_id']).sum()
city_ns.plot(kind = 'bar')
plt.xlabel('city_id')
plt.ylabel('item_cnt_month')
plt.show()
```
