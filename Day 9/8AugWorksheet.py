#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##ASSIGNMENT: Write a lambda function to round the numbers and then make use of the keyword round() and apply it using map
numbers= [1.34,4.56,6.78,10.90,8.45,6.75]


# In[18]:


numbers= [1.34,4.56,6.78,10.90,8.45,6.75]
d=list(map(round,numbers))
d


# In[14]:


numbers =[1.34,56.6,78.10,90.6,45.75]
d=lambda numbers:round(numbers)
list(map(d,numbers))


# In[19]:


numbers = [1.34,4.56,6.78,10.90,8.45,6.75]
print('Original numbers are:', numbers)
r = lambda x:round(x)
lst = list(map(r,numbers))
print('Rounded numbers are:', lst)


# In[28]:




def func(words, vowels): 
    final = [each for words in vowels if words in vowels] 
    print(final) 
    
words = ['inceptez','Students','clss','batch']
vowels = ['a','e','i','o']
func(words,vowels)


# In[31]:


x=[i for i in range(0,100) if i%7==0]
x


# In[32]:


x=[i*7 for i in range(0,100)]


# In[33]:


x


# In[ ]:




