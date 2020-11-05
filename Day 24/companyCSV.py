#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv("company.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.shape


# In[8]:


data.info()


# In[9]:


data.dtypes


# In[10]:


data.describe()


# In[11]:


data.describe(include="all")


# In[12]:


data.iloc[2:10,:]


# In[13]:


data.iloc[2:10,1:]


# In[14]:


data.loc[:,["Age","Salary"]]


# In[15]:


data[["Age","Salary"]]


# In[17]:


data.loc[9,"Salary"]


# In[18]:


data.loc[9,"Salary"] = 4300


# In[19]:


data.loc[9,"Salary"]


# In[20]:


data.rename(columns={"Company":"Organization"}, inplace = True)


# In[21]:


data


# In[22]:


data["Organization"].unique()


# In[23]:


data["Organization"].nunique()


# In[24]:


data["Organization"].value_counts()


# In[25]:


data.columns


# In[26]:


data.apply(lambda x : print(x.value_counts()) )


# In[27]:


data["Organization"].value_counts()


# In[28]:


data["Organization"]


# In[29]:


data["Organization"].value_counts()


# In[433]:


#regular expression


# In[434]:


#import re


# In[30]:


data


# In[31]:


data.duplicated().sum()


# In[32]:


data[data.duplicated()]


# In[33]:


data.drop_duplicates(inplace = True)


# In[34]:


data.shape


# In[35]:


data.dropna().shape


# In[36]:


data.dropna(subset=["Organization"], inplace = True)


# In[37]:


data.shape


# In[38]:


data["Age"].median()


# In[39]:


data["Age"].fillna(data["Age"].median(), inplace = True)


# In[40]:


data


# In[41]:


data.dropna(subset=["Salary"], inplace = True)


# In[42]:


data


# In[43]:


data.shape


# In[44]:


data[(data["Age"]>40) & (data["Salary"]<5000)]


# In[45]:


data["Age"].mean()


# In[46]:


data["Salary"].mean()


# In[47]:


data[["Age","Salary"]].apply(lambda x : x.mean())


# In[48]:


import matplotlib


# In[49]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[50]:


data["Salary"].plot(kind = "hist")


# In[51]:


data["Organization"].value_counts()


# In[52]:


data["Organization"].value_counts().plot(kind = "pie")


# In[53]:


data.groupby("Organization").Salary.mean()


# In[54]:


data


# In[62]:


X = data[["Age"]]
y = data["Salary"]


# In[63]:


from sklearn.model_selection import train_test_split


# In[64]:


train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3, random_state = 6)


# In[461]:


#val_X, test_X, val_y, test_y = train_test_split(test_X, test_y, test_size = 0.5, random_state = 9)


# In[65]:


train_X


# In[66]:


data.shape


# In[67]:


train_X.shape, test_X.shape, train_y.shape, test_y.shape


# In[68]:


import seaborn as sns


# In[69]:


data.plot(kind = "scatter", x = "Age", y = "Salary")


# In[70]:


from sklearn.linear_model import LinearRegression


# In[71]:


data.isna().sum()


# In[75]:


data=data.drop(columns="Place")


# In[77]:


data=data.drop(columns="Country")


# In[78]:


data


# In[79]:


model = LinearRegression()


# In[80]:


model.fit(train_X, train_y)


# In[81]:


model.intercept_


# In[82]:


model.coef_


# In[473]:


#Salary_pred = 91.02 + 95.66(Age)


# In[474]:


95.66*34 + 91.02 


# In[83]:


data.plot(kind = "scatter", x = "Age", y = "Salary")


# In[84]:


train_X


# In[85]:


pred_train = model.predict(train_X)


# In[ ]:





# In[86]:


import matplotlib.pyplot as plt


# In[87]:


plt.scatter(train_X,train_y, color = "green")
plt.scatter(test_X,test_y, color = "red")
plt.plot(train_X,pred_train, 'b' )


# In[88]:


pred_test = model.predict(test_X)


# In[89]:


from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# In[90]:


mean_squared_error(train_y, pred_train)


# In[91]:


mean_squared_error(test_y, pred_test)


# In[92]:


mean_absolute_error(train_y, pred_train)


# In[93]:


mean_absolute_error(test_y, pred_test)


# In[94]:


r2_score(train_y, pred_train)


# In[95]:


r2_score(test_y, pred_test)


# In[ ]:





# In[96]:


data_Org = pd.get_dummies(data["Organization"])


# In[97]:


data_new = pd.concat([data_Org,data[["Age","Salary"]]], axis = 1)


# In[98]:


X = data_new.drop(columns="Salary")


# In[99]:


y = data_new["Salary"]


# In[100]:




from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3, random_state = 6)

#val_X, test_X, val_y, test_y = train_test_split(test_X, test_y, test_size = 0.5, random_state = 9)

train_X

data.shape

train_X.shape, test_X.shape, train_y.shape, test_y.shape


# In[101]:


model = LinearRegression()

model.fit(train_X, train_y)


# In[102]:


model.intercept_


# In[103]:


model.coef_


# In[104]:


pred_train = model.predict(train_X)
pred_test = model.predict(test_X)


# In[105]:


from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("Train - MSE",mean_squared_error(train_y, pred_train))

print("Test - MSE",mean_squared_error(test_y, pred_test))

print("Train - MAE",mean_absolute_error(train_y, pred_train))

print("Test - MAE",mean_absolute_error(test_y, pred_test))

print("Train - R2 Score",r2_score(train_y, pred_train))

print("Test - R2 Score",r2_score(test_y, pred_test))


# In[106]:


data_new.corr()


# In[ ]:




