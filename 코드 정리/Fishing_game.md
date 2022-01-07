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

def game_fishing_center(df, id, pw):
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

```python
# 상점 구현 

def game_store (df, id, pw): 
    print("현재 판매하지 않은 물고기는 {}개 입니다.".format(len(df[(df['ID']==id)&(df['현황']=='미판')])))
    미판_index = df[(df['ID']==id)&(df['현황']=='미판')].index
    
    if len(미판_index) != 0:  # 판매 안 된게 있으면, 
        for i in range( len(미판_index)): 
            print("{} 물고기를 판매했어요.".format(df[(df['ID']==id)&(df['현황']=='미			 판')]['물고기'][미판_index[i]]))
            
       	    # DB 저장 / 엑셀 저장 
            df.loc[미판_index[i]]= [ id, pw, 
                                    df[(df['ID']==id)&(df['현황']=='미판')['물고기']									 [미판										_index[i]]],
                                    df[(df['ID']==id)&(df['현황']=='미판')['수량'] 								     [미판										_index[i]]],
                                    df[(df['ID']==id)&(df['현황']=='미판')['가격'] 								     [미판										_index[i]]],
                                    "판매"]
    else:  # 빈 경우 
        print("다 팔았네요, GOOD JOB")
 
    df.to_excel("./텍스트게임.xlsx", sheet_name="낚시게임", index=None)
```

```python
# 게임 플레이 및 사용자 정보 구하기 

def game_play(id, pw):
    
    while True: 
        df = pd.read_excel("./텍스트게임.xlsx")
        
        돈  = df[ (df['ID']==id)&(df["현황"]=="판매")]["가격"].sum()
        물고기_종류 = len(np.unique(df[df['ID']==id]['물고기'])) 
        잡은_물고기 = df[df['ID']==id]['수량'].sum()
        레벨 = len(df[(df['ID']==id)&(df['현황']=='판매')])
        
        if 레벨 <= 10: 
            레벨 = "낚시 연습생"
        elif 레벨 > 11 and 레벨 <=20: 
            레벨 = "낚시 신입생"
        elif 레벨 > 21: 
            레벨 = "낚시 "
            
        print("안녕하세요. {} 님 / 레벨 : {} / 가지고 있는 금액: {} / 잡은 물고기 종류: {} 		 / 잡은 물고기 수량: {}".
             format( id, 레벨, 돈, 물고기_종류, 잡은_물고기))
        
        선택 = int( input("낚시하기(1) / 상점이용(2) / 게임종료(3)" ))
        
        if 선택 == 1: # 낚시터 
            game_fishing_center(df, id, pw)
        elif 선택 == 2: # 상점 
            game_store(df, id, pw)
        elif 선택 == 3: #게임종료
            break       
```

```python
#계정정보

계정정보 = []
df = pd.read_excel('./텍스트게임.xlsx')

계정 = int(input('로그인 : 1 / 회원가입 : 2'))
print()

if 계정 == 1:
  계정정보.append(input('ID 입력 : '))
  계정정보.append(int(input('PW 입력 : ')))

  if 계정정보[0] in df['ID'].unique() and 계정정보[1] in df['PW'].unique():
    print()
    print('게임 시작')
    print()
    game_play(계정정보[0], 계정정보[1])
  else:
    print()
    print('일치하는 ID와 PW가 없음')
    print()
    pass
elif 계정 == 2:
  계정정보.append(input('ID 입력 : '))
  계정정보.append(int(input('PW 입력 : ')))
  print()
  print('회원가입 완료')
  print()
  print('게임 시작')
  game_play(계정정보[0], 계정정보[1])
```

