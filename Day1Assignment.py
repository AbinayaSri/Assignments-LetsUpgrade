#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as pyplot


# In[34]:


#Assignment 1 

x= np.arange(0,11)
y= x*x
pyplot.plot(x,y,color='green', marker='o', linestyle='dashed',linewidth=2, markersize=10)
pyplot.title("LinePlot")
pyplot.xlabel("xaxis")
pyplot.ylabel("yaxis")


# In[37]:


# Assignment 2 :Plotting Days against sales

a=[1,2,3,4,5,6,7]
b=[160,150,140,145,175,165,180]
pyplot.plot(a,b)
pyplot.title("Sales Vs WeekDay")
pyplot.xlabel("Day")
pyplot.ylabel("Sales")


# In[ ]:





# In[ ]:




