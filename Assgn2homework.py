#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[2]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get("https://www.naukri.com/jobs-in-delhi-ncr")


# In[5]:


soup=BeautifulSoup(driver.page_source,'html.parser')


# In[6]:


soup


# In[7]:


Job=soup.find_all('a',class_='title')
Job


# In[14]:


Job_list=[]
for i in Job[:16]:
    Job_list.append(i.text)
Job_list


# In[9]:


Company=soup.find_all('a',class_='comp-name mw-25')
Company


# In[12]:


Company_list=[]
for i in Company[]:
    Company_list.append(i.text)
Company_list


# In[34]:


dictt = {}
for i in range(len(Job_list)):
    dictt[Job_list[i]] = Company_list[i]

dictt
                 


# In[36]:





# In[ ]:




