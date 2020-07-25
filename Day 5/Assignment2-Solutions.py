#!/usr/bin/env python
# coding: utf-8

# ### The questions for the exercises are given above the cells and the expected output is given below the cell. Please type the code inserting a new cell below the question because if you run the expected output cell the output would vanish! Happy learning! 

# ## Exercise Question 1: Given a list1 copy the list1 to another list2 and remove the element at index 6 and add it to the 2nd position and also, at the end of the list2, finally remove the last element from list 1

# In[33]:


l1=[34, 54, 67, 89, 11, 43, 94]
print("Original list",l1)
l2=l1.copy()
print("The Copied List is:",l2)
a=l2.pop(4)
print("List After removing element at index 4",l2)
l2.insert(2,a)
print("List After Adding Element at index 2",l2)
l2.append(a)
print("List After Adding Element at Last",l2)
l1.pop()
print("Removing last element from the original list",l1)



# In[2]:





# ## Exercise Question 2: Given a two list of equal size create a list of unique elements from both the lists into a seperate list

# In[10]:





# In[36]:


l3=[2, 3, 4, 5, 6, 7, 8]
l4=[4, 9, 16, 25, 36, 49, 64]
print("First List:",l3)
print("Second List",l4)
list(set(l3+l4))

#l3=[2, 3, 4, 5, 6, 7, 8]
#l4=[4, 9, 16, 25, 36, 49, 64]
#print("First List:",l3)
#print("Second List",l4)
#l3.extend(l4)
#print(list(set(l3)))


# ## Exercise Question 3: Remove duplicate from a list and create a tuple and find the minimum and maximum number (Hint: Try Functions Min() and Max() ) 

# In[11]:





# In[41]:


l5=[87, 52, 44, 53, 54, 87, 52, 53]
print("Original list:",l5)
s1=set(l5)
print("Unique List:",list(s1))
t1=tuple(s1)
print("Tuple:",t1)
print("Minimum Number is:", min(t1))
print("Maximum Number is:", max(t1))


# ## Exercise Question 4: Display the each word in the string Count the number of words in a string and display it (Including the white spaces) 

# In[19]:


#Printing each words seperately 
a = "what's up?"
print(*a)


# In[18]:





# In[43]:


a="Welcome to Python"
print("The sample string:",a)
print("Printing each words seperately:",*a)
print("The Length of the string:",len(a))


# ##  Exercise Question 5: Write a Python program to access dictionary keys element by index. i.e. Use indexing methods to print the first key

# In[27]:





# In[44]:


d1= {'physics': 80, 'math': 90, 'chemistry': 86}
print("The dictionary is:",d1)
print("The key element accesed by index:",list(d1)[0])
#print(list(d1))


# In[ ]:




