#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


# Creating one dimensional array
arr = np.array([1, 2, 3])
print(arr)


# In[4]:


# Creating two dimensional array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)


# In[8]:


# Get dimensions of the array
arr.ndim


# In[9]:


# Get shape of the array
arr.shape


# In[10]:


# Get data type
arr.dtype


# In[11]:


# Get size
arr.itemsize


# In[15]:


# Get total size
# arr.size * arr.itemsize
# Or
arr.nbytes


# In[5]:


a = np.array([[1, 2, 3 , 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(a)


# In[6]:


# Getting little more customized output [startindex:endindex:stepsize]
a[0, 1:6:2]


# In[7]:


# All zeros matrix
np.zeros((2, 3))


# In[9]:


# All 1s matrix
np.ones((2, 3), dtype='int32')


# In[12]:


# Initializing matrix with any other value
np.full((2, 4), 16)


# In[14]:


# Making matrix with any other value (When the matrix is already created)
np.full_like(a, 5)


# In[15]:


# Initializing matrix with random decimal numbers
np.random.rand(4, 2)


# In[18]:


# # Initializing matrix with random decimal numbers
np.random.randint(8, size=(3,3))


# In[19]:


# Identity matrix
np.identity(3)


# In[24]:


# Repeating the array
arr = np.array([[1, 2, 3]])
rep = np.repeat(arr, 3, axis=0)
print(rep)


# ## Assignment

# In[33]:


# Printing the matrix using above concepts
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

output = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:-1, 1:-1] = z
print(output)


# ## Very important concept

# In[34]:


# Copying array
a = np.array([1, 2 ,3])
b = a.copy()
print(b)


# ## Mathematics

# In[36]:


arr = np.array([1, 2, 3, 4, 5])
print(arr)


# In[39]:


# Adding 2 to each element
arr + 2


# In[41]:


# Adding 2 to each element
arr += 2
print(arr)


# In[44]:


# Adding two arrays
arr1 = np.array([1, 2 ,5, 3, 1])
arrAdd = arr + arr1
print(arrAdd)


# In[46]:


# Taking square of each element in the array
a ** 2


# In[47]:


# Taking cosine of each element in the array
np.cos(a)


# ## Linear Algebra

# In[54]:


# Matrix multiplication of the matrices of different size
# No. of rows of one matrix must be equal to the no. of columns of the another matrix and vice versa
a = np.ones((2,3))
b = np.full((3,2), 2)

np.matmul(a,b)


# In[57]:


# Finding the determinant
a = np.identity(3)
np.linalg.det(a)


# ## Statistics

# In[61]:


# Finding the min from the array
stats = np.array([[1, 2, 3],[4, 5, 6]])
np.min(stats)


# In[62]:


# Finding the max from the array
np.max(stats)


# In[68]:


# Finding min from each row of the matrix
np.min(stats, axis = 1)


# In[72]:


# Finding min from each column of the matrix
np.min(stats, axis = 0)


# In[71]:


# Finding max from each row of the matrix
np.max(stats, axis = 1)


# In[73]:


# Finding min from each column of the matrix
np.max(stats, axis = 0)


# ## Reorganizing arrays

# In[76]:


# Reshaping the array
before = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(before)
after = before.reshape((4, 2))
print(after)


# In[77]:


# Reshaping the array
before = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(before)
after = before.reshape((2, 2, 2))
print(after)


# In[79]:


# Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

np.vstack([v1, v2, v2])


# In[81]:


# Horizontally stacking vectors
h1 = np.zeros((2, 4))
h2 = np.ones((2, 2))
np.hstack([h1, h2])


# ## Miscellaneous
# ### Load data from file

# In[88]:


# Loading data from file
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)


# ## Boolean masking and Advanced indexing

# In[90]:


# Boolean masking true if value is greater than 5
filedata > 5


# In[92]:


# Getting all of the values greater than 5
filedata[filedata > 5]


# In[93]:


# Checking the columns that have atleast one value greater than 5
np.any(filedata > 5, axis = 0)


# In[94]:


# Checking the columns that have all of the values greater than 5
np.all(filedata > 5, axis = 0)


# In[95]:


# Getting all of the values greater than 5 and less than 7
((filedata > 5) & (filedata < 7))

