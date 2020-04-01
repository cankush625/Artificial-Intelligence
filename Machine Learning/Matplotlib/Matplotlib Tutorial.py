#!/usr/bin/env python
# coding: utf-8

# ## Load necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ## Basic Graph

# In[4]:


# Plotting a simple graph
x = [2, 3, 4]
y = [3, 4, 5]

plt.plot(x, y)

plt.title('My First Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()


# In[18]:


# Plotting a simple graph and changing the font and fontsize
x = [0, 2, 3, 4, 5]
y = [0, 3, 4, 5, 6]

# Adding label to the plot, changing the color to red, changing the line width,
# Adding marker, changing the size of the marker and changing the color of the marker edge to blue
# Changing the linestyle to the dotted line
plt.plot(x, y, label = 'line', color = 'red', linewidth = 2, linestyle = '--', marker = '.', markersize = 10, markeredgecolor = 'blue')

plt.title('My First Graph', fontdict = {'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Changing tick marks size
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 1, 2, 3, 4, 5, 6])

# Adding legend
plt.legend()

plt.show()


# In[19]:


# Plotting a simple graph and changing the font and fontsize
x = [0, 2, 3, 4, 5]
y = [0, 3, 4, 5, 6]

# Using shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x, y, 'r.--', label = 'line')

plt.title('My First Graph', fontdict = {'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Changing tick marks size
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 1, 2, 3, 4, 5, 6])

# Adding legend
plt.legend()

plt.show()


# In[21]:


# Plotting a simple graph and changing the font and fontsize and adding second line
x = [0, 2, 3, 4, 5]
y = [0, 3, 4, 5, 6]

# Using shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x, y, 'b^--', label = 'line')

# Line number two
x2 = np.arange(0, 4, 0.5)
plt.plot(x2, x2**2)

plt.title('My First Graph', fontdict = {'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Changing tick marks size
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 1, 2, 3, 4, 5, 6])

# Adding legend
plt.legend()

plt.show()


# In[26]:


# Plotting a simple graph and changing the font and fontsize and adding second line
x = [0, 2, 3, 4, 5]
y = [0, 3, 4, 5, 6]

# Resize the graph
# Keep the dpi highest possible about in the range of 300 or 400
plt.figure(figsize = (5, 3), dpi = 300)

# Using shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x, y, 'b^--', label = 'line')

# Line number two
# Making second line with mixed style some continuous and some dotted
x2 = np.arange(0, 4, 0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label = 'line2')
plt.plot(x2[5:], x2[5:]**2, 'r--')

plt.title('My First Graph', fontdict = {'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Changing tick marks size
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 1, 2, 3, 4, 5, 6])

# Adding legend
plt.legend()

# Saving the graph
plt.savefig('myGraph.png', dpi = 300)

# Show plot
plt.show()

