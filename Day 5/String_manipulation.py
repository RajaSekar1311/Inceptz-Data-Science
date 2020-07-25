#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Mulitline strings
a = "Inceptez"
multi = """
this is also a string
that has multiple lines
"""


# In[5]:


print(multi+' '+a)


# ## Getting input from the user in python

# In[7]:


a = input()


# In[8]:


type(a)


# In[14]:


a = input("Please enter a string")


# In[15]:


a


# ## String Functions

# In[17]:


a.capitalize()


# In[20]:


a.upper()


# In[19]:


a.lower()


# In[21]:


a


# ## DO NOT FORGET TO ASSIGN IT BACK! 
# 

# In[24]:


a = a.upper()


# In[25]:


a


# In[28]:


# STrings you enter will be converted into bytes. This process is called as Encoding. All the strings are stored in Unicode format - UTF-8


# In[26]:


from encodings.aliases import aliases
aliases


# In[29]:


review = "I dont like this product"


# In[32]:


## b - bytes 
## r - raw


# In[31]:


review.encode("utf-8")


# In[34]:


review = "I dont like this product, This is the worst product ever!"
review.split()


# In[37]:


review = "I have been using mouse for long time doesnt work in my mac"
'mac' in review


# In[ ]:


review = "I have been using mouse for long time doesnt work in my mac"
'windows' in review


# ## Strip function

# In[39]:


review = "            I hate the product, Worst ever"


# In[40]:


review.lstrip()


# In[45]:


review ="*********************** ;;;;;;;;;]]]]]I hate the product, Worst ever"


# In[46]:


review.lstrip('* ;]')


# In[47]:


review ="I hate the product, Worst ever*********************** ;;;;;;;;;]]]]]"
review.rstrip('* ;]')


# In[48]:


review = "      one       hellof   a           product love it              "


# In[49]:


review.strip()


# ## JOIN FUNTION

# In[50]:


review.split()


# In[53]:


review= " ".join(review.split())


# In[52]:


"_____".join(review.split())


# In[54]:


review


# In[55]:


review.capitalize()


# In[56]:


review.replace("hellof","good")


# ## Fromatting

# In[57]:


mentor1 = "Laxmi"
mentor2 = "noor"
print("Python and statistics will be taught by mentor: {} . The ML and DL classes will be taught by {}.".format(mentor1,mentor2))


# In[60]:


mentor1 = "Laxmi"
mentor2 = "noor"
print("Python and statistics will be taught by mentor: {1} . The ML and DL classes will be taught by {0}.".format(mentor1,mentor2))


# In[ ]:




