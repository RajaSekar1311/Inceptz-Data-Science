#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1: Write a function to sort the list based on the first letter of the second element
# 
# lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
# 

# In[ ]:


lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
print("Original list:",lst)
print("Sorted list:",sorted(lst,key=lambda x:x[1]))


# In[1]:





# ## Exercise 2:  Write a function to sort the list based on the last letter of the second element
# 
# Use list from previous question

# In[ ]:



lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
print("Another Method \nOrginal List " ,lst)
slist=sorted(lst,key = lambda x:x[-1])
print("Sorted List ",slist)


# In[2]:





# ## Exercise 3: Create a range from 1 to 8 merge the given list and together to create a new list of tuples.
# 
# lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]

# In[ ]:



lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
lst3=[]
for i,j in zip(lst1,range(1,8)):
    a=(i,j)    
    lst3.append(a)
print(lst3)


# In[ ]:


lst= range(1,9)
lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
map1 = list(zip(lst1,lst))
print(map1,end =' ')


# In[3]:





# ## Exercise 4: Write a function and create a list consisted of the number of occurence of letter: a (all a's).
# 
# lst1=["Antartica", "America", "Armania", "Australia", "Albania", "Afganistan","Alaska"]

# In[ ]:



def cnt(word):
    cnt1=0
    for i in word:
        if 'a' in i or 'A' in i:
            cnt1+=1
    return(cnt1)
lst1=["Antartica", "America", "Armania", "Australia", "Albania", "Afganistan","Alaska"]
print(list(map(cnt,lst1)))


# In[4]:





# ## Exercise 5: Write a function filter all the vowels in a given string using filter.
# 
# str1="Inceptz is one of the best institutes to read data science in chennai"

# In[ ]:



str1="Inceptz is one of the best institutes to read data science in chennai"
vowels = ['a','e','i','o','u','A','E','I','O','U']

l1=[i for i in str1 for j in vowels if j in i]
print(l1)


# In[5]:





# ## Exercise 6:  Write a function to create a list as the square of elements from the given list if the square is greater than 60
# 
# lst1=[5, 6, 7 , 8, 9, 10, 12, 14]

# In[ ]:


lst1=[5,6,7,8,9,10,12,14]
l1=[i*i for i in lst1 if (i*i) > 60 ]
print(l1)


# In[6]:





# ## Exercise 7: take the words given below as list and write a function and use reduce to make it a sentence
# Inceptz 
# 
# provides
# 
# the
# 
# best
# 
# inclass 
# 
# trainings 
# 
# and
# 
# is 
# 
# the 
# 
# best
# 

# In[ ]:


words_= ["Inceptz","provides","the","best","inclass","trainings","and","is","the","best"]
from functools import reduce
lst =reduce(lambda x,y:x+" "+y,words_)
lst


# In[7]:





# In[ ]:




