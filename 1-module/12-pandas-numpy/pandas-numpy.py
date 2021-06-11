# %%
import pandas as pd
import numpy as np
# %%
a = pd.Series(np.random.random(10))
print(a)
# %%
a[0]
# %%
a[5]
# %%
colnames = ['Column1','Column2','Column3','Column4','Column5']
df = pd.DataFrame(np.random.random((10,5)), columns=colnames)
df
# %%
df['Column1']
# %%
df[['Column1','Column2','Column3']]
# %%
lst = [208500, 181500, 223500, 140000, 250000, 143000, 307000, 200000, 129900, 118000]
# %%
price_df = pd.DataFrame(lst, columns=['SalesPrice'])
price_df
# %%
lst_lst = [[8450, 'CollgCr', 2003, 7, 208500],
           [9600, 'Veenker', 1976, 6, 181500],
           [11250, 'CollgCr', 2001, 7, 223500],
           [9550, 'Crawfor', 1915, 7, 140000],
           [14260, 'NoRidge', 2000, 8, 250000],
           [14115, 'Mitchel', 1993, 5, 143000],
           [10084, 'Somerst', 2004, 8, 307000],
           [10382, 'NWAmes', 1973, 7, 200000],
           [6120, 'OldTown', 1931, 7, 129900],
           [7420, 'BrkSide', 1939, 5, 118000]]
# %%
colnames = ['LotSize','Neighboarhood','YearBuilt','Quality','SalePrice']
pd.DataFrame(lst_lst, columns=colnames)
# %%
house_dict = {'Baker House': [7420, 'BrkSide', 1939, 5, 118000],
              'Beazley House': [14115, 'Mitchel', 1993, 5, 143000],
              'Dominguez House': [14260, 'NoRidge', 2000, 8, 250000],
              'Hamilton House': [6120, 'OldTown', 1931, 7, 129900],
              'James House': [11250, 'CollgCr', 2001, 7, 223500],
              'Martinez House': [9600, 'Veenker', 1976, 6, 181500],
              'Roberts House': [9550, 'Crawfor', 1915, 7, 140000],
              'Smith House': [8450, 'CollgCr', 2003, 7, 208500],
              'Snyder House': [10084, 'Somerst', 2004, 8, 307000],
              'Zuckerman House': [10382, 'NWAmes', 1973, 7, 200000]}
# %%
pd.DataFrame(house_dict)
# %%
# You can transpose the result and adjust the colum names
house_df = pd.DataFrame(house_dict).transpose()
house_df.columns = colnames
house_df
# %%
# Or you can add the from_dict method and specify 'index'
# for the oriented parameter, and then adjust your column names.add()
house_df2 = pd.DataFrame.from_dict(house_dict, orient='index')
house_df2.columns = colnames
house_df2
# %%
# Aplicar funciones matemáticas a marcos de datos
# %%
# Total price of all house sold
house_df['SalePrice'].sum()
# %%
# Average lost size of house sold
house_df['LotSize'].mean()
# %%
# The latest year a house in the data se was built
house_df['YearBuilt'].max()
# %%
# The earliest year a house in the data set was built
house_df['YearBuilt'].min()
# %%
