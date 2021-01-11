import pandas as pd
df_moto = pd.read_csv('master.csv', dtype
df_moto['generation'].unique()

df_changed = pd.read_csv('master_changed2.csv', dtype='str')
df = pd.concat([df_moto, df_changed])
df = df.reset_index(drop=True)
df_gpby = df.groupby(list(df.columns))
idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
df.reindex(idx)



df_changed2 = pd.read_csv('master_changed2.csv', dtype='str')
df = pd.concat([df_changed, df_changed2])
df = df.reset_index(drop=True)
df_gpby = df.groupby(list(df.columns))
idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
df.reindex(idx)