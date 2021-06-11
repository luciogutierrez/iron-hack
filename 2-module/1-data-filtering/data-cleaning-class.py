# %%
import pandas as pd
import numpy as np
import re
from datetime import datetime


# %%
df = pd.read_csv('../../data-sets/marketing_data.csv')

# %%
df.head()

# %%
df.info()

# %%
# identicar nulos en la dataset por columna
df.isnull().sum()

# %%
df[df['Income'].isnull()==True]

# %%
col_names = df.columns
col_names

# %%
df.columns = df.columns.str.strip()
df.head()

# %%
df.columns

# %%
df[df['Income'].isnull()]

# %%
to_replace = [re.findall(r'Mnt.+', name)[0] for name in col_names if 'Mnt' in name]
to_replace

# %%
categories = [re.findall(r'(?<=Mnt).+', name)[0] for name in col_names if 'Mnt' in name]
categories

# %%
new_name_list = ['Amount_spent_in_'+name for name in categories]
new_name_list

# %%
dict_names = dict(zip(to_replace, new_name_list))
dict_names

# %%
df.rename(columns=dict_names, inplace=True)
df.columns

# %%
# función para limepieza de headers
def clean_columns(df):
    """
        function that receives a dataframe
        and cleas some columns names
    """
    col_names = df.columns
    df.columns = df.columns.str.strip()
    to_replace = [re.findall(r'Mnt.+', name)[0] for name in col_names if 'Mnt' in name]
    categories = [re.findall(r'(?<=Mnt).+', name)[0] for name in col_names if 'Mnt' in name]
    new_name_list = ['Amount_spent_in_'+name for name in categories]
    dict_names = dict(zip(to_replace, new_name_list))
    df.rename(columns=dict_names)
    return df

# %%
df2 = clean_columns(df)

# %%
df2.columns

# %%
df.columns

# %%
datetime.now()
# %%
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
# %%
# calcualndo la edad de los cliente
df['customer_age'] = datetime.now().year - df['Year_Birth']
df['customer_age']

# %%
df['Education'].unique()

# %%
def encode_education(var):
    if var == 'Basic':
        return 0
    if var == 'Graduation':
        return 1
    if var == 'Master':
        return 2
    if var == '2n Cycle':
        return 3
    if var == 'PhD':
        return 4
      
# %%
# apply funciona en series
df['Education_encoded'] = df['Education'].apply(encode_education)
df['Education_encoded']


# %%
df.head(5)

# %%
df['Income'] = df['Income'].apply(lambda x: re.sub(r'[$,]','', str(x)))
df['Income']

# %%
