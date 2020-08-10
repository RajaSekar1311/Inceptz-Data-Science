#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('orders.csv')
df.dtypes


# In[3]:


df['square']=[i*i for i in df['Meal Price']]
df.head()


# In[4]:


df.dtypes


# In[ ]:




