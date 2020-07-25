#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Tuple 
"""
1. () - Paranthesis , brackets ; [] - Square Brackets 
Common properties between list and tuple
2. Allows Heterogenous 
3. Retrive elements using index
Difference
4. Immutable, ,cannot be changed once declared
"""
samp_tuple = (1,2,2,"5",[1,6j])


# In[11]:


samp_tuple


# In[8]:


samp_tuple[2] =10


# In[12]:


samp_tuple.count(2)


# In[13]:


len(samp_tuple)


# In[15]:


samp_tuple.index('5')


# ### SET 
# { } - Flowe braces or Flower Brackets
# Common properties between a list, tuple and Set
#     1. Heterogenous 
#     
# Common properties between a set and a tuple:
#     1. immutable 
# 
# Properties of Set: 
#     1. Does not allow duplicates 
#     2. Cannot be accessed using Index 
#     3. Sometimes it can be ordered
#   

# In[17]:


sample_set = {1,2,5,7,3,4,20,10}


# In[18]:


sample_set


# In[19]:


sample_set[2]


# In[23]:


sample_set = {1,2,5,7,3,4,45,20,10,20,43,'a','b'}


# In[24]:


sample_set


# In[22]:


type(sample_set)


# In[45]:


#dictionary  --> Key and Value pairs
'''
1. Data is stored in terms of key value pairs 
2. Key is unique and the value can be duplicated 
3. Can retrieve the value using the key 
4. Values can be changed using the key 
5. key is immutable
'''
sample_dict = {'a':"alpha",1:"first",2:"Second",3:"third",4:'fourth','fourth':[20,20]}


# In[32]:


sample_dict[2]


# In[46]:


sample_dict


# In[34]:


sample_dict['New_key'] = 10


# In[35]:


sample_dict


# In[41]:


sample_dict[2] = 100


# In[42]:


sample_dict


# In[43]:


lst = [100,2,200,20]
lst[2] = 500


# In[44]:


lst


# In[53]:


#strings 
'''
1. Strings can be retrieved using index
2. Strings are immutable
'''
a = "Hi, how are you guys"
b = "Inceptez"


# In[49]:


a


# In[50]:


a[2] = 'k'


# In[54]:


a+' '+b


# In[55]:


## Type Conversion


# In[56]:


a = 10
print(type(a))


# In[57]:


a = float(a)
print(type(a))


# In[58]:


a


# In[59]:


s = 'Inceptez'
s = tuple(s)


# In[60]:


s


# In[62]:


s = 'Inceptez'
s = set(s)


# In[63]:


s


# In[64]:


a = 124
a = str(a)


# In[65]:


a


# In[66]:


a = "Hello"
a = int(a)


# In[67]:


lst1 = [[1,'one'],[2,'Two'],['a',['alpha','log']]]


# In[69]:


lst1[2][1][0]


# In[70]:


dict(lst1)


# In[71]:


lst1 = [1,2,4,5,6,7]
lst2 = lst1 


# In[72]:


lst2


# In[73]:


lst2[2] = 50


# In[74]:


lst2


# In[75]:


lst1


# In[76]:


lst2 = lst1.copy()


# In[77]:


lst1


# In[78]:


lst2


# In[79]:


lst2[2] = 20


# In[80]:


lst2


# In[81]:


lst1


# In[82]:


dic = {1: 'first', 2: 'Second', 3: 'third', 4: 'fourth', 'New_key': 10, 'a': 'alpha'}


# In[83]:


dic.keys()


# In[84]:


dic.values()


# In[ ]:




