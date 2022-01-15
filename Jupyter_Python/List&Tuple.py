#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Tuple
#항목이 1개일 때는 ,를 붙임
t6 =(1,)
type(t6)


# In[3]:


t6


# In[4]:


#모든 자료형 혼합가능
my = ['say', 2, ['coding', 'programming']]
my


# In[7]:


mys = ('say', 2, ['coding', 'programming'])
mys


# In[10]:


#값 존재 여부 확인
print(2 in mys)


# In[11]:


l = [1,3,'a',[10,20]]
len(l)


# In[12]:


#insert
todolist = ['기상', '세수', '양치']
todolist.insert(2, '아침식사')
todolist


# In[13]:


#extend
todolist.extend(['샤워', '드라마', '공부'])
todolist


# In[14]:


#삭제
#del 리스트명(인덱스)
del todolist[-1]
#리스트.remove(항목)
todolist.remove('양치')
todolist


# In[16]:


#pop
a = todolist.pop()
a #드라마
todolist


# In[21]:


wishlist = ['가방', '시계','신발']
mycart = []

#wishlist의 시계, 신발 추출해서 mycart에 담기
mycart.extend(wishlist[1:])
mycart

#wishlist의 시계, 신발 삭제
del wishlist[1:3]
wishlist
mycart


# In[24]:


#sorted
friends = ['이보성','이밍주','최근영']
sorted_friends = sorted(friends)
sorted_friends


# In[36]:


file_list = ['file1.py', 'file2.txt', 'file3.pptx']
name_extension = []

for i in file_list:
    #print(i.split('.'))
    name_extension.append(i.split('.'))
name_extension


# In[29]:


file_list = ['file1.py', 'file2.txt', 'file3.pptx']
name_extension = []
#file_list.split('.')
map(lambda x: x.split('.'), file_list)


# 학생별 총점,평균 구하기
# 다음은 학생 별 [국어,영어,수학]점수가 저장된 리스트이다.
# score_list = [[96,84,80],[96,86,76],[76,95,83],[89,96,69],[90,76,91]]
# 각 학생의 세 과목의 성적의 [총점, 평균]을 구하여 리스트에 담으시오.
# (평균은 반올림하여 소수점 1자리까지 표현한다.)

# In[39]:


score_list = [[96,84,80],[96,86,76],[76,95,83],[89,96,69],[90,76,91]]
stu_scores = []

for i in score_list:   
    #for문을 한 번 돌면 가로줄 한 번만 ([]안에는 그냥 통째로)
    #for문 안에 i,j 이렇게 두 개 두면 모두 다 돌음
    total = sum(i)
    avg = total / 3
    stu_scores.append([total, round(avg,1)])
    
stu_scoresscores


# 과목별 평균 구하기
# 다음은 학생 별 [국어,영어,수학]점수가 저장된 리스트이다.
# score_list = [[96,84,80],[96,86,76],[76,95,83],[89,96,69],[90,76,91]]
# 각 과목의 리스트를 분리하고 과목별 평균을 구해봅시다. 평균은 소수점 1자리까지 출력한다.

# In[48]:


score_list = [[96,84,80],[96,86,76],[76,95,83],[89,96,69],[90,76,91]]
kor_list=[]
eng_list=[]
math_list=[]

kor_average=0
eng_average=0
math_average=0
total = 0
for i in score_list:
    kor_list.append(i[0])
    eng_list.append(i[1])
    math_list.append(i[2])
    
kor_average = round(sum(kor_list) / len(score_list),1)
kor_average
eng_average = round(sum(eng_list) / len(score_list),1)
math_average = round(sum(math_list) / len(score_list),1)
print(kor_list, eng_list, math_list)
print(kor_average, eng_average, math_average)


# In[50]:


#random.choice(리스트명)
menulist = ['한식', '일식', '중식', '양식', '분식', '이탈리아식']
import random
random.choice(menulist)


# In[ ]:




