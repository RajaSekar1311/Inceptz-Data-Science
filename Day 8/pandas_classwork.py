#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install pandas')
import panda as pd
df=pd.read_CSV("https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv")
df.info()
df.olumn
df.shape()
df.desribe()
               


# In[14]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv")
df.info()
#df.column
df.shape
df.describe()


# In[15]:




df['city'].nunique()


# In[16]:


df['city'].unique()


# In[17]:


df['city'].value_counts()


# In[18]:


df['postal_code'].value_counts()


# In[20]:


df.loc([df['postal_code'].isin['94063','94401'])&(df['address_2']isna()==False])


# In[ ]:




