# %% [markdown]
# # Data Manipulation

# %%
import pandas as pd

# %%
data = pd.read_csv('../0-data/vehicles.csv')
data.head()

# %%
data.shape

# %%
# delete columns without data
data = data.dropna(axis=1)

# %%
# delete rows without data
data = data.dropna()

# %%
data.columns

# %%
# rename columns names
data = data.rename(columns={'Make': 'Manufacturer',
                            'Engine Displacement':'Displacement'})

# %%
column_order = ['Year', 'Displacement', 'Cylinders','Manufacturer', 'Model', 
       'Transmission', 'Drivetrain', 'Vehicle Class', 'Fuel Type',
       'Fuel Barrels/Year', 'City MPG', 'Highway MPG', 'Combined MPG',
       'CO2 Emission Grams/Mile', 'Fuel Cost/Year']
data = data[column_order]       
data.head()
# %%
