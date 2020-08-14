#!/usr/bin/env python
# coding: utf-8

# # Ex - GroupBy

# ### Introduction:
# 
# GroupBy can be summarizes as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)  
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# In[ ]:





# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 

# ### Step 3. Assign it to a variable called drinks.

# In[2]:


drinks=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv")


# In[3]:


drinks.head()


# ### Step 4. Which continent drinks more beer on average?

# In[9]:


drinks.groupby('continent')['beer_servings'].mean()


# ### Step 5. For each continent print the statistics for wine consumption.

# In[11]:


drinks.groupby('continent')['wine_servings'].describe()


# ### Step 6. Print the mean alcoohol consumption per continent for every column

# In[13]:


drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean()


# ### Step 7. Print the median alcoohol consumption per continent for every column

# In[14]:


drinks.groupby('continent')['total_litres_of_pure_alcohol'].median()


# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# In[17]:


drinks['spirit_servings'].mean()


# In[18]:


drinks['spirit_servings'].min()


# In[19]:


drinks['spirit_servings'].max()


# In[ ]:




