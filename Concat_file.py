import os
import pandas as pd
df=[]
for j,i in enumerate(os.listdir()):
    nome,exten=os.path.splitext(i)
    print(i)
    if exten == '.xlsx':
        df1=pd.read_excel(i)
        df.append(df1)
        
    else:
        continue
DataFrame=pd.concat(df)
DataFrame.head(10)
