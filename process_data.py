import pandas as pd
import json
import csv

＃币名：交易所生成字典
colnames=['coinname','exchange','volume','price','volume_percent'] 
data=pd.read_csv('output_7_4.csv',names=colnames, header=None)
for i in range(0, len(data)):
	data.loc[i,'volume'] = float(data.loc[i,'volume'].strip().replace('$','').replace(',',''))
#print(data.loc[:, 'volume'])
sum_volume=data.groupby(['coinname','exchange'])['volume'].sum()
a=sum_volume.reset_index()


d={}
l=len(a)
# for i in range(0,l):
print(l)
#generate a dictionary which has coinname and exchange name combination as key, and value is the column number
for i in range(0, len(a)):
	name = a.loc[i,'coinname']+':'+a.loc[i,'exchange']
	d[name] = i
# print(a.loc[0,'coinname']+':'+a.loc[0,'exchange'])
# print(a.loc[2,'coinname']+':'+a.loc[2,'exchange'])

with open('dict.json', 'w') as fp:
    json.dump(d, fp)
