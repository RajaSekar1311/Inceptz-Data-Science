#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("Enter the Dividend:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest Divisor is:",a[0])


# In[ ]:




