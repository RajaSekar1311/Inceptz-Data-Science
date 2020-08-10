#!/usr/bin/env python
# coding: utf-8

# # Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[2]:


chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv",sep = "\t")


# ### Step 4. See the first 10 entries

# In[3]:


chipo.head(10)


# ### Step 5. What is the number of observations in the dataset?

# In[4]:


chipo.info()


# ### Step 6. What is the number of columns in the dataset?

# In[5]:


chipo.shape


# ### Step 7. Print the name of all the columns.

# In[6]:


chipo.columns


# ### Step 8. How is the dataset indexed?

# In[7]:


chipo.index


# ### Step 9. Which was the most ordered item?

# In[14]:


chipo['item_name'].value_counts


# ### Step 10. How many items were ordered?

# In[26]:


chipo['quantity'].sum()


# ### Step 11. What was the most ordered item in the choice_description column?

# In[10]:


chipo['choice_description'].value_counts


# ### Step 12. How many items were orderd in total?

# In[13]:


chipo['quantity'].sum()


# ### Step 13. Turn the item price into a float

# In[58]:


chipo.dtypes
chipo['item_price']=chipo['item_price'].astype(float)
chipo.dtypes


# In[67]:


chipo['item_price'] = chipo['item_price'].replace('$', '')
chipo['item_price']
chipo.head(10)


# ### Step 14. How much was the revenue for the period in the dataset?

# In[68]:


chipo['item_price'].sum()


# ### Step 15. How many orders were made in the period?

# In[22]:


chipo['order_id'].value_counts().count()


# ### Step 16. What is the average amount per order?

# In[69]:


sumorder = chipo.groupby(['order_id']).sum()
sumorder.mean()


# ### Step 17. How many different items are sold?

# In[70]:


chipo['item_name'].value_counts().count()


# In[ ]:




