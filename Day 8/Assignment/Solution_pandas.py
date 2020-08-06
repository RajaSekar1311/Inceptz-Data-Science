#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 

# In[ ]:





# In[18]:


import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df=pd.DataFrame(exam_data,index=['a','b','c','d','e','f','g','h','i','j'])
print(df)


# In[1]:





# ## Exercise 2: Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
# ##### Use Data from previous problem

# In[13]:


res=df[(df['attempts']<2) & (df['score']>15)]
print("Number of attempts in the examination is less than 2 and score greater than 15 :",res)


# In[2]:





# ## Exerise 3: Change the value in row 'd' to 11.5 
# ##### Use Data from previous questions

# In[14]:


print("Original data frame:",df)
updf=df.loc['d','score']=11.5
print("Change the score in row 'd' to 11.5:",updf)


# In[3]:





# ## Exercise 4: Write a Pandas program to calculate the sum of the examination attempts by the students. (Question continuation of data from question 2)
# ##### Use Data from previous questions

# In[16]:


sum_df=df['attempts'].sum()
print("The sum of the examination attempts by the students:",sum_df)


# In[ ]:





# ## Exercise 5: Drop a list of rows from a specified DataFrame
# ###### data: 
# d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

# In[39]:


d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df2=pd.DataFrame(d)
print(df2)
print("New DataFrame after removing 2nd & 4th rows:\n", df2.drop([2,4]))


# In[5]:





# ## Exercise 6: Write a function that checks whether a given column is present in a DataFrame or not
# ###### data: 
# d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
# 
# Check if col4 and col1 is present

# In[47]:


print("Original DataFrame:", df2)
if 'col1'in df2.columns:
    print("Col1 is present in DataFrame")
else:
      print("Col1 is not present in DataFrame")
if 'col4'in df2.columns:
    print("Col4 is present in DataFrame")
else:
      print("Col4 is not present in DataFrame")


# ## Exercise 7: Write a function that returns the column index number from column name of a given DataFrame
# 
# ###### data: 
# d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
# 
# ##### HINT: Try using a function called get_loc():
# Syntax: 
# dataframe.columns.get_loc()

# In[49]:


print("Original DataFrame:", df2)
print("Index of 'Col2':",df2.columns.get_loc('col2'))


# In[8]:





# ## Exercise 8: Write a Pandas program to select all columns, except one given column in a DataFrame.
# ###### Use same data as previous problem

# In[57]:


print("Original DataFrame:", df2)
print("All columns except 'col3':\n",df2.iloc[:,df2.columns!='col3'])


# In[9]:





# ## Exercise 9:  Write a Pandas program to remove last n rows of a given DataFrame.

# In[59]:


print("Original DataFrame:", df2)
print("After removing last 3 rows of the said DataFrame:",df2.iloc[:3])


# In[10]:





# ## Exercise 10: Display the movies longer than 30 minutes and shorter than 360 minutes
# use IMDB-Movie-Data.csv

# In[65]:


import pandas as pd
df3 = pd.read_csv('IMDB-Movie-Data.csv')
subdf = df3[['Title', 'Runtime (Minutes)']]
result = subdf[(subdf['Runtime (Minutes)'] >= 30) & (subdf['Runtime (Minutes)'] <= 360)]
print("List of movies longer than 30 minutes and shorter than 360 minutes:")
print(result)


# In[15]:





# In[ ]:




