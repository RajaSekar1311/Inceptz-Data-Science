#!/usr/bin/env python
# coding: utf-8

# # Ex2 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

# In[5]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/jokecamp/FootballData/master/UEFA_European_Championship/Euro%202012/Euro%202012%20stats%20TEAM.csv). 

# ### Step 3. Assign it to a variable called euro12.

# In[6]:


euro12=pd.read_csv("https://raw.githubusercontent.com/jokecamp/FootballData/master/UEFA_European_Championship/Euro%202012/Euro%202012%20stats%20TEAM.csv")


# ### Step 4. Select only the Goal column.

# In[7]:


euro12


# In[8]:


euro12['Goals']


# ### Step 5. How many team participated in the Euro2012?

# In[11]:


euro12['Team'].shape


# ### Step 6. What is the number of columns in the dataset?

# In[12]:


euro12.info()


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[16]:


discipline=euro12[['Team', 'Yellow Cards','Red Cards']]
discipline


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[18]:


discipline=discipline.sort_values(['Red Cards','Yellow Cards'])
discipline


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[19]:


discipline['Yellow Cards'].mean()


# ### Step 10. Filter teams that scored more than 6 goals

# In[26]:


euro12[euro12['Goals']>6]


# ### Step 11. Select the teams that start with G

# In[36]:


euro12.loc[[5,6]]


# ### Step 12. Select the first 7 columns

# In[32]:


euro12.iloc[:,0:7]


# ### Step 13. Select all columns except the last 3.

# In[33]:


euro12.iloc[:,:-3]


# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[34]:


euro12.loc[[3,7,12] , ['Team','Shooting Accuracy']]


# In[ ]:




