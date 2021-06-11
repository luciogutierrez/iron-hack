# %%
import pandas as pd
import numpy as np

# %%
data = pd.read_csv('master.csv')
data.info()

# %%
data.head(5)

# %%
data.columns
# %%
data.shape
# %%
set(data['country'])
# %%
len(set(data['country']))

# %%
data.pivot_table(index='year', columns='sex', values='suicides_no', aggfunc=['sum','mean','median','max','min'])
# %%
data.pivot_table(index=['country','year'], columns='sex', values='suicides_no', aggfunc='sum')

# %%
data.pivot_table(index='year', columns='sex', values='suicides_no', aggfunc='sum')

# %%
data[data['year']==2016].head(10)

# %%
data[data['year'] >= 2016].head(10)

# %%
data[(data['year'] >= 2016) & (data['year'] <= 2018)].head(10)

# %%
print(len(set(data['country'][data['year']==2015])))
print(len(set(data['country'][data['year']==2016])))
# %%
data2 = data[data['year']!=2016]

# %%
data2.groupby('sex').agg({'suicides_no':'sum'})

# %%
data2.groupby(['sex']).agg({'suicides_no':['sum','max']})

# %%
data2.groupby(['sex']).agg({'suicides_no':'sum', 'population':'max'})

# %%
data2.groupby(['age']).agg({'suicides_no':'sum'})

# %%
data3 = data2.groupby(['age']).agg({'suicides_no':'sum', 'population':'sum'})
data3.head()

# %%
data3['suicides_no']/data3['population']
# %%
data3['suicides_no']/data3['population'].sort_values(ascending=True)

# %%
data_country = data2.groupby('country').agg({'suicides_no':'sum', 'population':'sum'})
data_country.head()
# %%
data_country['avg_suicide'] = data_country['suicides_no']/data_country['population']

# %%
data_country.sort_values(by='avg_suicide', ascending=False).head(10)

# %%
