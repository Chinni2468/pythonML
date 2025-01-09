#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum / counter
    return mean


# In[5]:


#find the product of given numbers
def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result 


# In[6]:


product(2,4,6,8,10)


# In[7]:


mean_value(4,6,8)


# In[ ]:




