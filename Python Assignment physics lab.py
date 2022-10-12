#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy as np

def fred (a,b):
    c = (a + b)*12
    return c 

a = 13.2 
b = 3.9 
c = fred(a,b)
print("c = ", c)



# In[109]:


def rule3(dA, dB):
    dQ = np.sqrt(dA**2 + dB**2)
    return dQ
dA = 12
dB = 33
dQ = rule3(dA, dB)
print("dQ = ", dQ)


# In[110]:


## example of an actual lab use 

x = np.array([1, 1.1, 1.2, 1.3])
y = x*3
print(y)
ysq = y**2
print(ysq)


err_x = np.std(x)/np.sqrt(4)
avg_x = np.average(x)
print(avg_x, err_x)


# ### This is latek 
# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$
# 
# 
# $\frac{\delta A} {A}$

# ### This is the assignment
# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$
# 
# 
# $\delta V_i = \sqrt{(\frac{\delta X} {X})^2 + (\frac{\delta 2Y} {2Y}})^2$
# 

# In[111]:


def rule1(C,dA):
    dQ = C * dA
    return dQ

C = 12
dA = 12
dQ = rule1(C,dA)
print(dQ)


# In[112]:


def rule2(C,M,A,dA):
    dQ = C * M * (A**(M-1)) * dA
    return dQ
C = 1
M = 2
A = 5
dA = 10
dQ = rule2(C,M,A,dA)
print(dQ)


# In[113]:


def rule3(dA, dB):
    dQ = np.sqrt(dA**2 + dB**2)
    return dQ
dA = 10
dB = 10
dQ = rule3(dA, dB)
print(dQ)


# In[114]:


def rule4 (M,dA,A,N,dB,B):
    dQ = np.sqrt(((M * dA)/(A))**2 + ((N * dB)/(B))**2)
    return dQ
M = 1
dA = 2
A = 1
N = 1
dB = 2
B = 1
dQ = rule4(M,dA,A,N,dB,B)
print(dQ)


# In[115]:


x = np.array([1.1, 1.3, 1.4, 0.9, 0.95, 1.05 ])

avg = np.average(x)
std = np.std(x)
print("The average of the data is:", avg, "and the standard deviation is:",std)

