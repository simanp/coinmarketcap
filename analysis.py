import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as dates

df=pd.read_csv('big_data.csv')
pf=pd.read_csv('price.csv')
df3 = df.filter(regex='^bitcoin:')
print(df3.sum(axis=1))

# print(df3.shape)

#找出交易量变化比较大的交易所
# def findoutlier(coinname, ratio=2.0):
#     df3 = df.filter(regex='^%s:' % coinname)
#     for column in df3:
#         m=df3[column].mean()
#         s=df3[column].std()
#         for i in range(0,len(df3)):
#             if df3.loc[i,column]>(m+ratio*s):
#                 print(df.iloc[i,0],column,'is a outlier')
#每天变化的比例
def changepercent(coinname):
    df3 = df.filter(regex='^%s:' % coinname)
    r=df3.shape[0]-1
    c=df3.shape[1]
    df_percent = pd.DataFrame(np.zeros(r*c).reshape(r,c),columns=df3.columns)
    for i in range(0,df3.shape[1]):
        for j in range(1,df3.shape[0]):
            if df3.iloc[j-1,i]!=0:
                p=(df3.iloc[j,i]-df3.iloc[j-1,i])/df3.iloc[j-1,i]
                df_percent.iloc[j-1,i]=p
    return df_percent
print(changepercent('bitcoin'))
