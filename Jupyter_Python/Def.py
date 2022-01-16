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


# In[12]:


def get_plus(n1,n2):
    return n1+n2

print(get_plus(1,2))


# In[13]:


#소수 여부 판단하기
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):  #1은 소수라서
        if n % i == 0:
            return False
    return True
is_prime(17)


# In[ ]:




