```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime

```


```python
# 데이터 불러오기
sales = pd.read_csv('sales_train.csv')
items = pd.read_csv('items.csv')
item_categories = pd.read_csv('item_categories.csv')
shops = pd.read_csv('shops.csv')
test = pd.read_csv('test.csv')
```

## 1. 전처리


```python
sales
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
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2935844</th>
      <td>10.10.2015</td>
      <td>33</td>
      <td>25</td>
      <td>7409</td>
      <td>299.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2935845</th>
      <td>09.10.2015</td>
      <td>33</td>
      <td>25</td>
      <td>7460</td>
      <td>299.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2935846</th>
      <td>14.10.2015</td>
      <td>33</td>
      <td>25</td>
      <td>7459</td>
      <td>349.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2935847</th>
      <td>22.10.2015</td>
      <td>33</td>
      <td>25</td>
      <td>7440</td>
      <td>299.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2935848</th>
      <td>03.10.2015</td>
      <td>33</td>
      <td>25</td>
      <td>7460</td>
      <td>299.00</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>2935849 rows × 6 columns</p>
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

    ERROR! Session/line number was not unique in database. History logging moved to new session 739
    




    0         2013-01-02
    1         2013-01-03
    3         2013-01-06
    4         2013-01-15
    5         2013-01-10
                 ...    
    2935844   2015-10-10
    2935845   2015-10-09
    2935846   2015-10-14
    2935847   2015-10-22
    2935848   2015-10-03
    Name: date, Length: 2928469, dtype: datetime64[ns]




```python
sales.shape # (2935849, 6)
```




    (2935849, 6)




```python
sales.corr() # 상관계수
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


    
![png](output_19_0.png)
    



    
![png](output_19_1.png)
    



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


    
![png](output_21_0.png)
    



    
![png](output_21_1.png)
    



```python

```
