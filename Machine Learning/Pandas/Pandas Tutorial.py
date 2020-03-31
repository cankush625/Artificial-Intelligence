#!/usr/bin/env python
# coding: utf-8

# ## Loading data into Pandas

# In[3]:


import pandas as pd


# In[39]:


# Reading csv file
df = pd.read_csv('pokemon_data.csv')


# In[ ]:


# Reading excel file
df_xlsx = pd.read_excel('pokemon_data.xlsx')


# In[ ]:


# Reading data from tab separated file or text file
df_tab = pd.read_csv('pokemon_data.txt', delimiter = '\t')


# In[8]:


# See top rows
df.head()


# In[9]:


# See bottom rows
df.tail()


# ## Reading data in Pandas

# In[10]:


# Reading headers
print(df.columns)


# In[14]:


# Read each column
print(df['Name'])

# OR
print(df.Name)


# In[13]:


# Read first five names in the column
print(df['Name'][0:5])


# In[15]:


# Reading two or more columns by the column names
print(df[['Name', 'Type 1', 'Type 2']])


# In[16]:


# Reading single row
print(df.iloc[1])


# In[18]:


# Reading multiple rows
# Using iloc
print(df.iloc[0: 4])


# In[19]:


# Reading a specific location (R, C)
print(df.iloc[2, 1])


# In[ ]:


# Reading data from each row
for index, row in df.iterrows():
    print(index, row['Name'])


# In[22]:


# Reading specific data
# Using loc
print(df.loc[df['Type 1'] == 'Fire'])


# ## Sorting/Describing data

# In[23]:


# Describing data
df.describe()


# In[24]:


# Sorting data
df.sort_values('Name')


# In[25]:


# Sorting data in descending order
print(df.sort_values('Name', ascending = False))


# In[26]:


# Sorting values by taking multiple parameters into consideration
print(df.sort_values(['Type 1', 'HP']))


# In[27]:


# Sorting values by taking multiple parameters into consideration, where first parameter is sorted in ascending order and second parameter is sorted in descending order
print(df.sort_values(['Type 1', 'HP'], ascending = [1, 0]))


# ## Making changes to the data

# In[28]:


# Adding total column to the dataframe and giving it values as the total of the stats
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head())


# In[35]:


# Dropping a column from the dataframe
df = df.drop(columns = ['Total'])
print(df.head())


# In[40]:


# Adding total column to the dataframe and giving it values as the total of the stats using
df['Total'] = df.iloc[:, 4 : 10].sum(axis = 1)
print(df.head())


# In[41]:


# Changing the position of the columns in the dataframe
cols = list(df.columns)
df = df[cols[0 : 4] + [cols[-1]] + cols[4 : 12]]
df.head()


# In[43]:


# Saving modified dataframe to the csv file
df.to_csv('modified_pokemon.csv', index = False)


# In[ ]:


# Saving modified dataframe to the excel file
df.to_excel('modified_pokemon.xlsx', index = False)


# In[ ]:


# Saving modified dataframe to the text file
df.to_csv('modified_pokemon.txt', index = False, sep = '\t')


# ## Filtering data

# In[45]:


# Reading rows having pokemon with type1 as Grass and type2 as Poison
# In Pandas we have to use actual and sign(&)
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]


# In[48]:


# Reading rows having pokemon with type1 as Grass or type2 as Poison
# In Pandas we have to use actual or sign(|)
df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]


# In[51]:


# Reading rows having pokemon with type1 as Grass and type2 as Poison and HP greater than 70
# In Pandas we have to use actual and sign(&)
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df


# In[54]:


# Resetting index in new detaframe
new_df = new_df.reset_index(drop = True)
new_df


# In[55]:


# Resetting index in new detaframe and making changes inplace
new_df.reset_index(drop = True, inplace = True)
new_df


# In[56]:


# Reading all the records which contains string 'Mega' in their name
df.loc[df['Name'].str.contains('Mega')]


# In[57]:


# Reading all the records that not contains string 'Mega' in their name
# In pandas, for not we use tild sign(~)
df.loc[~df['Name'].str.contains('Mega')]


# In[59]:


# Using regular expressions to read the records having type1 as grass or fire
import re

df.loc[df['Type 1'].str.contains('Grass|Fire', regex = True)]


# In[60]:


# Using regular expressions to read the records having type1 as grass or fire and ignoring the case
df.loc[df['Type 1'].str.contains('grass|fire', flags = re.I, regex = True)]


# In[61]:


# Using regular expressions to read the records containing pi in the Name and ignoring the case
df.loc[df['Name'].str.contains('pi[a-z]*', flags = re.I, regex = True)]


# In[62]:


# Using regular expressions to read the records Starting with pi in the Name and ignoring the case
df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I, regex = True)]


# ## Conditional changes

# In[66]:


# Replacing or changing the type1 as Flammer from Fire
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
df

# Replacing or changing the values of two columns at same time if total is greater than 500
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = [1, 'True']
df
# ## Aggregate Statistics(Groupby)

# In[71]:


# Grouping the records
df.groupby('Type 1').mean()


# In[72]:


# Grouping the records and reading the records by sorting according to the highest defense
df.groupby('Type 1').mean().sort_values('Defense', ascending = False)


# In[73]:


# Adding the records by grouping them
df.groupby('Type 1').sum()


# In[74]:


# Counting the number of records by grouping them
df.groupby('Type 1').count()


# In[76]:


# Adding count column and adding count values to it
df['Count'] = 1
df.groupby(['Type 1']).count()['Count']


# In[77]:


# Grouping by multiple columns and adding count column and adding count values to it
df['Count'] = 1
df.groupby(['Type 1', 'Type 2']).count()['Count']


# ## Working with large amount of data

# In[81]:


# Working on large amounts of data
new_df = pd.DataFrame(columns = df.columns)
for df in pd.read_csv('modified_pokemon.csv', chunksize = 5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])

