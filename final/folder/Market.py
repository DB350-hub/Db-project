#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
conn = sqlite3.connect('Database.db')

# ### S&P500

# In[21]:
#
#
# SnP = pd.read_csv("^GSPC.csv")
# SnP.head(5)
# SnP.isnull().sum()
# SnP
#
#
# # ### NASDAQ
#
# # In[20]:
#
#
# NDQ = pd.read_csv("^IXIC.csv")
#
#

# ### RUSSELL2000

# In[19]:
cur = conn.execute("SELECT * from nasdaq")
a = cur.fetchall()
df = pd.DataFrame(a,columns = ["date","open","high","low","adj_close","volume"])
df.drop(["volume"],inplace =True,axis = 1)
print(df.head(5))


# In[ ]:
