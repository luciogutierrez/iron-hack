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
# %%
