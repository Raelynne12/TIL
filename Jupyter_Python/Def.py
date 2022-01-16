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


# In[14]:


#위치인수
def greet(name, msg):
    print('hi', name, msg)
    
greet('friend','long time no see')


# In[16]:


#디폴트인수
def greet(name, msg = '오랜만이야'): #1번째에 넣으면 안됨 >> 기본 인수 다 쓴 뒤
    print('hi', name, msg)
    
greet('friend')
greet('friend','long time no see')


# In[18]:


#키워드인수
def get_minus(x,y,z):
    return x-y-z
print(get_minus(5,15,10))
print(get_minus(5, z = 15, y = 10)) #순서 바꿔서 가능 >> 얘도 기본인수 다 쓴 뒤


# In[19]:


#가변인수
def average(args):
    return sum(args) / len(args)
average([1,2,3])


# In[20]:


#매개변수에 * 붙이면 여러 개 인수를 하나의 튜플로 받음
def average(*args):
    return sum(args) / len(args)

average(1,2,3)


# In[21]:


print(1,2,3, sep = '@')


# In[ ]:




