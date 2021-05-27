# %%
import pandas as pd
import numpy as np

# %%
data = pd.read_csv('../../data-sets/database_liquors.csv')

# %%
# descripción de la data
data.info()

# %%
data['date'].head(20)

# %%
data['date'].dtypes

# %%
np.dtype('datetime64[ns]') == np.dtype('<M8[ns]')

# %%
# convert object to date
data['date'] = pd.to_datetime(data['date'])

# %%
# cambiar nombre de campo
data = data.rename(columns={'invoice':'invoice_id'})

# %%
# longitud de dataset
len(data)

# %%
data['mes'] = data['date'].dt.month
data['año'] = data['date'].dt.year
data[['mes','año']]

# %%
data['año_mes'] = data['date'].values.astype('datetime64[M]')
data['año_mes']

# %%
df1 = data.groupby(['item_description','category_name','county','año_mes']).agg({'bottles_sold':'sum','sale_usd':'sum'}).reset_index()
df1.head(10)

# %%
# .loc (subset de set mas grandes)
df1 = df1.set_index('item_description')

# %%
list(df1.index.unique())

# %%
df1.loc[['1800 Anejo']]

# %%
df1.loc[['1800 Anejo','Havana Club Anejo Blanco']].head(10)

# %%
df1.loc['1800 Anejo':'Havana Club Anejo Blanco', ['category_name','sale_usd']].head(10)

# %%
df1.loc[df1['sale_usd']>10000, ['bottles_sold','sale_usd']]

# %%
# iloc - busqueda de enteros
df1.iloc[4]

# %%
df1.iloc[[4, 400, 4000]]

# %%
# por indice en rows y tambien en columnas
df1.iloc[[2,100],[0,4]]

# %%
df1.iloc[2:100,[0,4]].head(10)

# %%
df1.iloc[2:100,[0,4]].reset_index().head(10)

# %% [markdown]
# ## Descriptive Statistics

# %%
import matplotlib.pyplot as plt

# %%
df1.head()

# %%
df1.describe()

# %%
df1.groupby('item_description')[['sale_usd','bottles_sold']].mean()

# %%
df2 = df1.groupby('item_description')[['sale_usd','bottles_sold']].mean()

# %%
plt.figure(figsize=(20,10))
df2.boxplot(column=['sale_usd'])

# %%
plt.figure(figsize=(20,10))
df2.boxplot(column=['bottles_sold'])

# %%
df2[df2['bottles_sold'] > 1750]

# %%
df2.describe(percentiles=[.2,.4,.6,.8])

# %%
import numpy as np
q1, q3 = np.percentile(df2['bottles_sold'],[25,75],axis=0)
iqr = q3 - q1
upper = q3 + (iqr * 3)
lower = q1 - (iqr * 3)
print(q1)
print(q3)
print(iqr)
print(upper)
print(lower)
# %%
# borrar lo que este por arriba del upper
df3 = df2.drop(df2[df2['bottles_sold']>upper].index).reset_index()
df3

# %%
df3.head(1)

# %%
df3[df3['item_description'].str.contains('Anejo')].sort_values('sale_usd',ascending=False)
# %%
