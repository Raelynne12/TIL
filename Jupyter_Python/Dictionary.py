#!/usr/bin/env python
# coding: utf-8

# In[1]:


menu = dict(김밥=2000, 떡볶이 = 5000, 튀김 = 2000)
menu


# In[3]:


#zip()
key = ['김밥','떡볶이','어묵','튀김']
value = [2000,2500,2000,3000]
menu2 = dict(zip(key,value))
menu2


# In[4]:


menu3 = dict([('김밥',2000),('떡볶이',2500),('어묵',2000),('튀김',3000)])
menu3


# In[5]:


#key값에 튜플도 가능
number=7

dict1 = {
    100:'hundred',
    True:'참',
    False:'거짓',
    (1,3):'학년,반',
    number:'번호'
}
print(dict1)


# In[6]:


menu.get('햄버거', '존재하지않음')


# In[7]:


#setdefault
scores = {'kor':100, 'eng':90, 'math':80}

# music점수 90점 추가
scores.setdefault('music',90)  #이미 값이 있으면 변경되지 않음

scores


# In[8]:


scores = {'kor':100, 'eng':90, 'math':80}

# math:90, music:90
scores.update(zip(['math','music'],[90,90]))

scores


# In[12]:


scores = {'kor':100, 'eng':90, 'math':80}

# 키가 'kor'인 항목 삭제
del scores['kor']

scores


# In[13]:


scores = {'kor':100, 'eng':90, 'math':80}

# 키가 'kor'인 항목의 값 받아온 후 삭제
kor = scores.pop('kor')

print(kor)
print(scores)


# In[16]:


scores.keys()
scores.values()
scores.items()


# In[17]:


#for문으로 딕셔너리 키만 출력
for i in scores.keys():
    print(i)
    #그냥 scores라고만 해도 기본은 키값이 나옴


# In[18]:


#for문으로 둘 다 출력
scores = {'kor':100, 'eng':90, 'math':80}
for i in scores.items():
    print(i)


# In[19]:


#키 정렬
#sorted()


#sort는 지원하지 않음 >> sorted로 해야


# 영어단어장 만들기
# 엔터를 입력할 때까지 영어단어,뜻을 입력받아 단어장을 만들고, 입력이 끝나면 단어 테스트를 실시하는 프로그램을 만들어봅시다.
# 1) 단어장을 만듭니다.
# 2) 단어테스트를 실시하고 맞은 갯수를 계산합니다.
# 3) 테스트가 끝나면 맞은갯수/전체단어수/점수 형태로 결과를 출력합니다

# In[26]:


#단어장 만들기
#enter입력할 때까지 영어단어, 뜻 입력받아서 딕셔너리에 저장
dict_word = {}
while True:
    input_word = input('영어단어와 뜻 입력 : ')
    if input_word == '':
        break

    else:
        eng = input_word.split(',')[0]  #쉼표 앞 eng
        kor = input_word.split(',')[1]  #쉼표 뒤 kor
        dict_word[eng] = kor    #key = value
    
dict_word


# In[27]:


#단어테스트
cnt = 0
for eng, kor in dict_word.items():
    answer = input(eng)
    if answer == kor:
        print('O')
        cnt += 1
    else:
        print('X')


# In[28]:


#테스트 결과 출력
print('맞은 개수 : ', cnt)
print('전체문제수 : ', len(dict_word))
print('점수 : ', round(cnt/len(dict_word) * 100, 1))


# In[ ]:




