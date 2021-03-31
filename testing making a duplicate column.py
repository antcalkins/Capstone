import pandas as pd

df = pd.read_csv('IHDB_30-03-2021_23-24-04.csv')
df_dups = df[df.duplicated(['md5', 'sha256', 'sha1'])]
dataframe_list = list(df.columns)
dups = df_dups['Unnamed: 0']
print(dataframe_list)
print(dups)
duplicates = []
for i in range(0, len(df)):
    if i in dups:
        duplicates.append(True)
    else:
        duplicates.append(False)
print(duplicates[62])
df['duplicates'] = duplicates
print(df.head())