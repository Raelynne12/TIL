# Fishing Game

> 배웠던 파이썬 기본 문법들을 가지고 간단한 게임 만들어보기
>
> \>> 낚시 게임



```python
import time
import random
import numpy as np
import pandas as pd
```

```python
#낚시터 구현하기

fishing = pd.read_excel('./물고기표.xlsx')
fishing.info()							#null값 있는지 확인, 0~750, 자료형 확인

def game_fishing_center():
    print('낚시게임 시작')
    
    choose_fish = np.array(fishing).reshape(-1,4)	#-1 << 레코드에 있는 거 전부 다
    choose_fish_num = random.randint(0, len(fishing))	#0부터 전체 행까지 반복
    choose_fish_waiting_num = random.randint(choose_fish[choose_fish_num][0], 		choose_fish[choose_fish_num][1])
    
    time.sleep(choose_fish_waiting_num)		#대기시간 추가
    print()
    print('낚시 성공')
    print()
    print('{}님이 낚은 물고기는 {}입니다.'.format(id, choose_fish[choose_fish_num]		[2]))
    
    #DB 저장 / 엑셀 저장
    df.loc[len(df)] = [id, pw, choose_fish[choose_fish_num][2], 1, 					[choose_fish_num][-1], '미판매']
    df.to_excel('./텍스트게임.xlsx', sheet_name = '낚시게임', index = None)
```

