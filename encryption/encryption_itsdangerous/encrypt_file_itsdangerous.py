#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing pandas
import pandas as pd


# In[14]:


#file defination
file=r'c:/users/91734/Desktop/data.csv'
#dataframe creation by importing csv file
df1 = pd.read_csv(file)
print(df1)


# In[3]:


#importing encryption module
from itsdangerous import URLSafeSerializer


# In[4]:


#start decryption
#encryption done only for name and place
s = URLSafeSerializer('secret-key')
for i in range(0,df1.shape[0]):
    print("decrypting value", df1['name'][i])
    df1['name'][i] = s.dumps(df1['name'][i])
    print("decrypting value", df1['place'][i])
    df1['place'][i] = s.dumps(df1['place'][i])


# In[9]:


#printing after decryption
print(df1)

