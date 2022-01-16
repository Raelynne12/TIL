#!/usr/bin/env python
# coding: utf-8

# In[3]:


def introduce():
    print('hi')
    print('my name is python')
    
introduce()


# In[9]:


def introduce(name):
    print('안녕하세요')
    print('저의 이름은, '+name+'입니다.')

introduce('이한열')


# In[11]:


name = input('이름 : ')
age = input('나이 : ')

def happybir(name, age):
    print(f'{name}님의 {age}번째 생일을 축하합니다.')
    #f를 써야 들어감
    
happybir(name, age)


# In[ ]:




