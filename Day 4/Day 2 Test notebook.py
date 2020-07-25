#!/usr/bin/env python
# coding: utf-8

# # BASICS OF PYTHON
# ## Each Box is called Cell
# ## Group of Cells are called Kernel
# 

# In[1]:


import keyword
keyword.kwlist 


# # Rules For Identifiers
# 
# 1. Identifiers can't be a keyword.
# 2. It can't start with a number.
# 3. It Should not contain special Characters.
# 4. Spaces are not allowed
# 5. Case Sensitive
# 6. Underscores are allowed
# 

# # Data Types
# 
# 1. Number
# 2. string
# 3. Boolean
# 4. list
# 5. tuple
# 6. set
# 7. dictionary

# # 1. Number - Integer, Float, Complex

# In[2]:


a = 10
print(type(a))


# In[3]:


b=06.04
print(type(b))


# In[4]:


c=1+2j
print(type(c))


# # 2. String

# In[5]:


d="raja"
print(type(d))


# In[10]:


#multi line string
e="""Sekar"""
type(e)


# # 3. Boolean

# In[12]:


f=True
type(f)
print(type(f))


# # 4. List

# In[8]:


l1=[1,2,45,56,20,10]
l1.sort()
l1


# In[9]:


l2=[4,5.6,'raja',2,1]
l2


# # List Operations- Functions/Methods in list 

# In[13]:


l2.append([8,9])
l2


# In[14]:


l2.extend([10,21])
l2


# In[15]:


l2.extend([[6,7]])
l2


# In[16]:


a=l2.pop()
a


# In[17]:


b=l2.pop(3)
b


# In[21]:


l2.remove(4)
l2


# In[30]:


l2.remove(5.6)
l2


# In[31]:


l2.remove(10)
l2


# In[32]:


l2.remove(1)
l2


# In[33]:


l2.remove(0)
l2


# In[34]:


l2.remove([8,9])
l2


# # List Slicing

# In[35]:


l3=[6,3,27,8,9,10,22,'ravi']
l3


# In[36]:


l3[1]


# In[37]:


l3[:-1]


# In[38]:


l3[2:4]


# In[39]:


l3[0:8]


# In[40]:


l4=l3[0:5]


# In[41]:


l4


# In[42]:


l3[:0]=20
l3


# In[45]:


l3[2:3]=[100,200]


# In[46]:


l3


# In[47]:


l3[2]=[100,200]
l3


# In[48]:


l3[3:5]=[100,200]
l3


# In[49]:


l3[5:8]=[100,200]
l3


# In[50]:


l4[:0]=20
l4


# In[51]:


l4[-1]=[2,3]
l4


# In[52]:


l4[-3:]


# In[53]:


l4[:-2]


# In[56]:


l4[1:3]=[]


# In[57]:


l4


# In[ ]:




