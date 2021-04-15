# %%
import pandas as pd
df = pd.read_csv('./vehicles.csv')

def get_means(df):
    numeric = df._get_numeric_data()
    means = pd.DataFrame(numeric.mean()).reset_index()
    means.columns = ["Column","Mean"]
    return means

mean_df = get_means(df)
mean_df



# %%
