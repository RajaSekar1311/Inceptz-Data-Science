#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1: Convert a list and tuple into arrays

# In[19]:


import numpy as np
lst=[1,2,3,4,5,6,7,8]
print("List to Array")
print(np.asarray(lst))
#l1=lst[0:3]
l2=lst[3:8:2]
#t=tuple(l1+l2)
t=([8,4,6],[1,2,3])
print("Tuple to array")
#a=np.asarray(t)
#print(a.reshape(2,3))
print(np.asarray(t))


# In[20]:


import numpy as np
lst=[1,2,3,4,5,6,7,8]
print("List to Array")
print(np.asarray(lst))
t=([8,4,6],[1,2,3])
print("Tuple to array")
print(np.asarray(t))


# In[6]:





# ## Also try np.asarray for the problem above! 

# ## Exercise 2:  Convert the values of Centigrade degrees into Fahrenheit degrees

# In[28]:


lst=[ 0.,12., 45.21, 34., 99.91]
print("Values in Fahrenheit Degrees:")
farray=np.asarray(lst)
print(farray)
print("Values in Centigrade Degrees:")
print((5*farray)/9 - (5*32)/9)


# In[4]:





# ## Exercise 3: Write a NumPy program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements. 

# In[39]:


lst=[3,5.0,7]
a=(np.asarray(lst))
print("Size of the array:",a.size)
print("Length of one array element in bytes:",a.itemsize)
print("Total bytes consumed by the elements of the array:",a.nbytes)


# In[7]:





# ## Exercise 4: Get the unique elements of an array

# In[65]:


a=np.asarray([10,10,20,20,30,30])
print("Original Array:",a)
print("Unique elements of the above array:",np.unique(a))
b=np.asarray([[1,1],[2,3]])
print("Original Array:",b)
print("Unique elements of the above array:",np.unique(b))


# In[9]:





# ## Exercise 5: Change the dimension of an array
# 

# In[45]:


lst=[1,2,3,4,5,6,7,8,9]
a=np.asarray(lst)
print("Original array:",a)
ra=a.reshape(3,3)
print("The Dimension of Array with 3 rows and 3 columns:",ra)


# In[42]:





# ## Exercise 6: Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive

# In[48]:


print(np.linspace(2.5,6.5,30))


# In[12]:





# ## Exercise 7: Convert 1-D arrays as columns into a 2-D array

# In[70]:


a1=np.array([10,20,30])
a2=np.array([40,50,60])
print("Array1:",a1)
print("Array1:",a2)
a=np.stack((a1,a2),axis=1)
print("Converted Array:",a)


# In[21]:





# ## Exercise 8: Create a 5x5 matrix with row values ranging from 0 to 4

# In[80]:


a=np.zeros((5,5))
print("Original Array:",a)
a[0:5,1:5]=1,2,3,4
print("Row values ranging from 0 to 4:",a)


# In[22]:





# ## Exercise 9: Sum of all the multiples of 3 or 5 below 100

# In[96]:


a=np.arange(1,100)
n= a[(a % 3 == 0) | (a % 5 == 0)]
print(n[:100])
print(n.sum())


# In[23]:





# ## Exercise 10: Combine a one and a two dimensional array together and display their elements
# ##### Hint : np.nditer()

# In[102]:


import numpy as np
x = np.arange(4)
print("One dimensional array:")
print(x)
y = np.arange(8).reshape(2,4)
print("Two dimensional array:")
print(y)
for a, b in np.nditer([x,y]):
    print("%d:%d" % (a,b),)


# In[29]:





# ## Exercise 11: Write a NumPy program to replace all elements of NumPy array that are greater than specified array.

# In[98]:


a=np.array([[0.42436315,0.48558583,0.32924763],[0.7439979 ,0.58220701,0.38213418],[0.5097581,0.34528799,0.1563123 ]])
print("Original array:",a)
print("Replace all elements of the said array with .5 which are greater than .5")
a[a>.5]=.5
print(a)


# In[30]:





# ## Exercise 12: Add a new row to an empty numpy array

# In[109]:


a=np.array([])
print("Empty array:",a)
a1=np.array([10,20,30])
a2=np.array([40,50,60])
print("After adding two new arrays:",np.stack((a1,a2)))


# In[110]:





# Empty array:
# []
# After adding two new arrays:
# [[10 20 30]
#  [40 50 60]]

# ## Exercise 13: Write a NumPy program to join a sequence of arrays along a new axis. 

# In[116]:


a1=np.array([1,2,3])
a2=np.array([2,3,4])
print("Original Arrays:")
print(a1)
print(a2)
print("Sequence of arrays along a new axis:",np.stack((a1,a2)))
a3=np.array([[1],[2],[3]])
a4=np.array([[2],[3],[4]])
print("Original Arrays:")
print(a3)
print(a4)
print("Sequence of arrays along a new axis:",np.vstack((a3,a4)))


# In[35]:





# In[ ]:




