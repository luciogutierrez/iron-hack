# %% [markdown]
# # Pandas data analysis


# %%
import numpy as np
import pandas as pd

# %%
student = pd.read_csv('../../data-sets/student-mat.csv')
# %%
student.info()

# %%
student.dtypes()

# %%
student.describe()
# %%
pd.crosstab(index=student['sex'], columns='count')

# %%
pd.crosstab(index=student['sex'], columns=student['activities'])
# %%
pd.crosstab(index=student['address'], columns=student['famsize'])

# %%
student['improvement'] = np.where(student['G2'] > student['G1'], 'improved', 'did not improve')
student['improvement']
# %%
pd.crosstab(index=student['school'], columns=student['improvement'])
# %%
student.pivot_table(index='school', columns=['sex','studytime'], values='G3', fill_value=0)
# %%
# with aggregate function
student.pivot_table(index='school', columns=['sex','studytime'], values='G3', fill_value=0, aggfunc='count')
# %%
