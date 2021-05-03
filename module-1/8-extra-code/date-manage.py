# %%
# import numpy and pandas
import numpy as np
import pandas as pd
# %%
# do a range of 10 dates day by dat
days = pd.date_range("2021-01-01", periods=10, freq='D')
days
# %%
# do a dict with date, store and sales (random)
a = pd.DataFrame({"date":days,
                    "store":"a",
                    "sales": np.random.randint(100,200,size=10)})

b = pd.DataFrame({"date":days,
                    "store":"b",
                    "sales": np.random.randint(100,200,size=10)})                    

c = pd.DataFrame({"date":days,
                    "store":"c",
                    "sales": np.random.randint(100,200,size=10)})                    
# %%
# combine the 3 df with concat
df = pd.concat([a, b, c]).sort_values(by="date")
#df.sort_values(by="date")
df.head()
# %%
# applying rank function such an order for date
df["rank"] = df.groupby("date")["sales"].rank(ascending=False).astype("int")
df.head(6)
# %%
# rank can be used to make a comparison between the stores
df.groupby(["store","rank"]).count()[["sales"]]
# %%
# here is how result looks without selecting a column
df.groupby(["store","rank"]).count()
# %%
# using a named aggregation with de agg function
# we need to specify name of the columns and the aggregations function
df.groupby(["store","rank"]).agg(rank_count = ("rank", "count"))
# %%
# The index is an important part of a dataframe so it needs to be accurate.
# one option is to reset the index after the connectenation
df = pd.concat([a, b, c]).sort_values(by="date").reset_index(drop=True)
df.head()
# %%
# Also can use ignore index parameter
df = pd.concat([a, b, c]).sort_values(by="date", ignore_index=True)
df.head()
# %%
