import pandas as pd
df=pd.read_excel('A.xlsx')

print(df)

df= df.set_index(df.columns[0])

from bioinfokit import analys, visuz
visuz.gene_exp.hmap(df=df,rowclus=False, colclus=False, dim=(3,6), tickfont=(6,4))
