#!/usr/bin/env python
# coding: utf-8

# In[30]:


#import pandas as pd

#df = pd.read_csv('C:/Users/Zng/Desktop/Pokemon.csv',delimiter='\t')
#print(df)

#print(df.tail(3))

#print(df.columns)

#print(df['Name'][0:5])

#print(df.Name)

#print(df[['Name', 'Type', 'Hp']])

#print(df.iloc[0:1])

#for index, row in df.iterrows():
#    print(index, row['Name'])

#df.loc[df['Type 1'] == "Grass"]

#df.sort_values('Name', ascending=False )

#df['Total'] = df['Total'] + df['Total'] + df['Total'] 

#df.drop(columns=['Total'])

#df['Total'] = df.iloc[:,4:9].sum(axis=1)

#cols = list(df.columns.values)
#df = df[cols[0:4]] + cols[-1]

#df.to_csv('modified.csv', index=False)
filtetring 
#

#

#

#

#

#
#
#


# In[18]:



#ldpq = np.array(['Cu','In','Sn',110,120,130])

#print(ldpq)

#ldpq.ndim (dimension)

#ldpq.shape

#ldpq.itemsize

#ldpq.d(type)

#ldpq[2] #ldpq[0,:]

#np.zeros((2,3))

#math, statistic and more


#ADDING MODE

#a = np.array(['Cu', 'In', 'Sn'])

#b = np.array(['DBTL'])

#np.char.add(a, b)
#array(['CuDBTL', 'InDBTL', 'SnDBTL'], dtype='<U6')


#np.concatenate((a, b), axis=0)
#array(['Cu', 'In', 'Sn', 'DBTL'], dtype='<U4')


# a = np.array(['Cu', 'In', 'Sn'])
# b = np.array(['DBTL'])
# np.insert(a, 2 --> THE POSITION THAT YOU WANT TO PUT IT, b)
# array(['Cu', 'In', 'DB', 'Sn'], dtype='<U2')

#

#

#

#

#

#


#ldpq1 = ldpq.reshape((3 --> amount rows ,2 --> amount rows))

#v1
#v2
#np.vstack9([v1,v2,v2,v2])

#filedata = np.genfromtxt('data.txt', delimiter=',')


# In[16]:


import pandas as pd
import numpy as np


# In[52]:


ldpq = np.array(['Cu','In','Sn',110,120,130])
print(ldpq)
ldpq1 = ldpq.reshape((2,3))


# In[53]:


ldpq1 = ldpq.reshape((2,3))


# In[57]:


pd.DataFrame(ldpq1)


# In[41]:





# In[42]:





# In[ ]:




