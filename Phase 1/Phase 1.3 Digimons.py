#%%
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#%%

df=pd.read_csv('../src/DigiDB_digimonlist.csv', index_col=0)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#%%
df
# %%
print("\n Los nulos del conjunto de datos son: \n")
nulos = pd.DataFrame(df.isnull().sum() / df.shape[0] * 100, columns = ["%_nulos"])
display(nulos[nulos["%_nulos"] > 0])

print("\n Los duplicados son: \n")
display(df.duplicated().sum())
    
# %%
