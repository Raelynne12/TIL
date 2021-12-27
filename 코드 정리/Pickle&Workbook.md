# pickle

> 데이터를 저장하고 불러올 때 매우 유용한 라이브러리
>
> 클래스 자체를 통째로 파일로 저장했다가 그대로 불러오기 가능
>
> 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장



**pickle로 저장하고 읽기**

````python
import pandas as pd
import pickle
temp = pd.DataFrame({'a':[1], 'b':[2]})
temp.to_pickle('./iampickle.pkl')
pd.read_pickle('./iampickle.pkl')
````

