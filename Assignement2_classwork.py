#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[5]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[7]:


driver=webdriver.Chrome()


# In[8]:


driver.get('https://www.flipkart.com/search?q=iphone+13&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&as-pos=2&as-type=RECENT&suggestionId=iphone+13%7CMobiles&requestId=e1abe2e4-7c32-465a-a524-a845cf5de383&as-searchtext=iphone%2013')


# In[9]:


soup=BeautifulSoup(driver.page_source,'html.parser')


# In[10]:


soup


# In[11]:


names="KzDlHZ"
price="Nx9bqj _4b5DiR"
rating="XQDdHH"


# In[12]:


phone_name=soup.find_all('div',class_=names)
phone_price=soup.find_all('div',class_=price)
phone_rating=soup.find_all('div',class_=rating)


# In[13]:


phone_name


# In[14]:


phone_name_list=[]
for i in phone_name:
    phone_name_list.append(i.text)


# In[15]:


phone_name_list


# In[16]:


phone_price_list=[]
for i in phone_price:
    phone_price_list.append(i.text)


# In[17]:


phone_price_list


# In[18]:


phone_rating_list=[]
for i in phone_rating:
    phone_rating_list.append(i.text)


# In[19]:


phone_rating_list


# In[20]:


driver.quit()


# In[27]:


phone_dict = {}
for i in range(len(phone_name_list)):
    phone_dict[phone_name_list[i]] = {
        'price': phone_price_list[i],
        'rating': phone_rating_list[i]}

print(phone_dict)


# In[28]:


import pandas as pd


# In[31]:


d=pd.DataFrame(phone_dict)
d.to_csv("assgn2classwork.csv")


# In[32]:


d


# In[34]:


import os


# In[35]:


print(os.getcwd())


# In[36]:


print(os.listdir(os.getcwd()))


# In[ ]:




