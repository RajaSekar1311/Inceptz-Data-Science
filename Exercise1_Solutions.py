#!/usr/bin/env python
# coding: utf-8

# ### The questions for the exercises are given above the cells and the expected output is given below the cell. Please type the code inserting a new cell below the question because if you run the expected output cell the output would vanish! Happy learning! 

# ## Exercise Question 1: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

# In[2]:


list1=[34,54,67,89,11,43,94]
print("Original List",list1)
a=list1.pop(4)
print("List After Removing Element at index 4:",list1)
list1.insert(2,a)
print("List After Ading Element at Index 2:",list1)
list1.append(a)
print("List After Adding Element at Last:",list1)


# ## Exercise Question 2: Given a Python list you should be able to display Python list in the following order

# In[3]:


list2=[100,200,300,400,500]
print("The Original List is:", list2)
list2.sort(reverse=True)
#list2.reverse()
print("The Result After Reverse Sorting:", list2)


# ## Exercise Question 3: Concatenate (join) two lists in the following order
# 

# In[4]:


list3=['Hello', 'take']
print("The List3 Contains:", list3)
list4=['Dear', 'Sir']
print("The List4 Contains:", list4) 
#list3.extend(list4)
print("The concatinated list is:",list3+list4)


# ## Exercise Question 4: Add item 7000 after 6000 in the following Python List

# In[24]:


list5=[10,20,[300,400,[5000,6000],500],30,40]
print("The Original List is:",list5)
list5[2][2].append(7000)
print("The List After insertion:",list5)


# ## Exercise Question 5: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the

# In[25]:


list6=['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
print("The Original List is:",list6)
list6[2][1][2].extend([["h","i","j"]])
print("The List After Insertion:",list6)
#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


# ## Exercise Question 6: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# In[26]:


list7=[5,10,15,20,25,50,20]
print("The Original List is:",list7)
a=list7.index(20)
list7[a]=200
print("The List After Replacement is:", list7)


# In[ ]:




