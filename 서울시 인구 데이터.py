#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


pop_seoul = pd.read_csv('C:\\Users\\chodaeheeUniverse\\Downloads\\데이터분석\\파이썬\\report.txt', sep='\t')


# In[13]:


pop_seoul.head()


# In[46]:


pop_seoul = pd.read_csv('C:\\Users\\chodaeheeUniverse\\Downloads\\데이터분석\\파이썬\\report.txt', sep='\t', header=2, thousands=',')
pop_seoul.head()


# In[47]:


pop_seoul=pop_seoul[['자치구','계','남자','여자','계.2','65세이상고령자']]
pop_seoul.head()


# In[48]:


pop_seoul.columns = ['구','전체','남자','여자','외국인','65세이상']
pop_seoul.head()


# In[49]:


pop_seoul.drop([0], inplace = True)
pop_seoul.head()


# In[50]:


pop_seoul['외국인비율'] = pop_seoul['외국인'] / pop_seoul['전체'] * 100
pop_seoul['고령자비율'] = pop_seoul['65세이상'] / pop_seoul['전체'] * 100
pop_seoul.head()


# In[51]:


pop_seoul.sort_values(by='전체', ascending=False).head(5)


# In[52]:


pop_seoul.sort_values(by='외국인비율', ascending=False).head(5)


# In[53]:


pop_seoul.sort_values(by='고령자비율', ascending=False).head(5)


# In[54]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[55]:


from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False


# In[56]:



font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
#matplotlib.rc('font', family="NanumBarunGothic")


# In[57]:


pop_seoul.set_index('구', inplace=True)
pop_seoul.head()


# In[59]:


pop_seoul['전체'].sort_values().plot(kind='barh', grid=True, figsize=(10,10));


# In[61]:


pop_seoul['65세이상'].sort_values().plot(kind='barh', grid=True, figsize=(10,10));


# In[63]:


pop_seoul['고령자비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10));


# In[64]:


pop_seoul['외국인비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10));

