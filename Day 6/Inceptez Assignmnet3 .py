#!/usr/bin/env python
# coding: utf-8

# ### The questions for the exercises are given above the cells and the expected output is given below the cell. Please type the code inserting a new cell below the question because if you run the expected output cell the output would vanish! Happy learning! 

# ## 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 

# In[1]:





# In[9]:


lst1=[]
for i in range(1500,2701):
    if i%5==0 and i%7==0:
        lst1.append(i)
print (lst1)


# In[46]:


lst1=[]
for i in range(1500, 2701):
    if i%7==0 and i%5==0:
        lst1.append(str(i))
print (','.join(lst1))


# ## 2. Write a Python program to construct the following pattern, using a nested for loop.
# 

# In[3]:





# In[28]:


for i in range(1,6): 
    print(str('*') * i)
for j in range(i,0,-1):
    print(str('*') * j)
  
    


# In[31]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# ## 3. Write a Python program to count the number of even and odd numbers from a series of numbers.

# In[4]:





# In[42]:


lst=[43,55,66,88,71,37,92,100,13]
lst1=[]
lst2=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
        even=len(lst1)   
    else:
        lst2.append(i)
        odd=len(lst2)   
print("Number of Even numbers:",even)
print("Number of odd numbers:",odd)


# In[45]:


lst=[43,55,66,88,71,37,92,100,13]
even=0
odd=0
for i in lst:
    if i%2==0:
        even+=1   
    else:
        odd+=1  
print("Number of Even numbers:",even)
print("Number of odd numbers:",odd)


# ## 4. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

# In[5]:





# In[65]:


lst5=[]
for i in range(100,401):
    stri=str(i)
    if (int(stri[0])%2==0) and (int(stri[1])%2==0) and (int(stri[2])%2==0):
        lst5.append(stri)
#print(lst5)
print(','.join(lst5))  


# ## 5. Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

# In[7]:





# In[27]:


HAge = int(input("Input a dog's age in human years: "))

if HAge < 0:
    print("Age must be positive number.")
    exit()
elif HAge <= 2:
    DAge = HAge*10.5
else:
    DAge = 21+(HAge-2)*4

print("The dog's age in dog's years is", DAge)


# ## 6. Write a Python function to find the Max of three numbers.

# In[69]:


def maxofthreeno(a,b,c):
        print("The Three Numbers are:",(a,b,c))
        print(max(a,b,c))

maxofthreeno(3,6,-5)


# ## 7. Write a Python function that takes a number as a parameter and check the number is prime or not.

# In[11]:





# In[22]:


def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print("The Number is:",n)
                print("False")
                break
        else:
            print("The Number is:",n)
            print("True")
    else:
        print("The Number is:",n)
        print("False")
prime(9)


# ## 8. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# 

# In[13]:





# In[77]:


str2="Inceptz is One of The BeSt Places TO LEarn DataSciEnce"
print("Original String:",str2)
upper=0
lower=0
for i in str2:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print("No. of Upper ase Charaters:",upper)
print("No. of lower ase Charaters:",lower)


# ## 9. Write a Python program to reverse a string. 

# In[19]:





# In[71]:


st1="1234abcd"
print("The Original String is:",st1)
print("The Reversed String is:",st1[::-1])
      


# ## 10. Write a Python program to find  the greatest common divisor (gcd) of two integers.

# In[18]:





# In[25]:


def GCD(n1,n2):
    if n2==0:
        return n1
    else:
        return (GCD(n2,n1%n2))
n1=int(input())
n2=int(input())
print("The two numbers are:",(n1,n2))
result=GCD(n1,n2)
print("The GCD ofthe numbers are:",result)


# In[26]:


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)


# In[ ]:




