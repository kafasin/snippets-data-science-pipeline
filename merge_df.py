import pandas as pd

df1 = pd.DataFrame(dict(a=[1,2,3], b=[10,20,30], col_to_merge=["a","b","c"]))
df2 = pd.DataFrame(dict(d=[10,20,100], col_to_merge=["a","b","c"]))

df_merged = df1.merge(df2, on='col_to_merge')
