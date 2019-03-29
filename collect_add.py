import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import datetime

debug_mode = False

data = []
if not debug_mode:
    with open('website_cryptomarket.csv','r') as f:
        reader=csv.reader(f)
        for rl in reader:
            r = requests.get(rl[0])
            soup = BeautifulSoup(r.text, 'lxml')
            table = soup.find('table', id='markets-table')
            for row in table.find_all('tr'):
                try:
                    exchange = row.find('a', class_='link-secondary').text
                    volume = row.find('span', class_='volume').text.strip()
                    price = row.find('span', class_='price').text.strip()
                    volume_percent = row.find('span', {'data-format-percentage':True}).text
                except AttributeError:
                    continue
                coinname=rl[0].split('/')[4]
                #print([coinname,exchange,volume,price,volume_percent])
                data.append([coinname,exchange,volume,price,volume_percent])
    colnames=['coinname','exchange','volume','price','volume_percent'] 
    data=pd.DataFrame(data, columns=colnames)
    #print(data.head())
    for i in range(0, len(data)):
        data.loc[i,'volume'] = float(data.loc[i,'volume'].strip().replace('$','').replace(',',''))
        data.loc[i,'price'] = float(data.loc[i,'price'].strip().replace('$','').replace(',',''))
    df = data.groupby(['coinname','exchange'])
    price=df['price'].sum()/df['price'].count()
    sum_volume = df['volume'].sum()
    #print(data.groupby(['coinname','exchange'])['price'].to_string())
    new_grouped=sum_volume.reset_index()
    price_grouped=price.reset_index()
    print(price_grouped.head())
   

with open('dict.json', 'r') as fp:
    d = json.load(fp)
v=[-1.0]*(len(d)+1)
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
v[0]=st

if not debug_mode:
    for i in range(0, len(new_grouped)):
        name = new_grouped.loc[i,'coinname']+':'+new_grouped.loc[i,'exchange']
        if name in d:
            j = d[name] + 1
            if j >= 0 and j < len(v):
                v[j]=new_grouped.loc[i,'volume']
            else:
                print("Warning: invalid index " + str(j) + " for '" + name + "'")
        else: 
             print("not found the '" + name + "'")        
u=[-1.0]*(len(d)+1)
u[0]=st
if not debug_mode:
    for i in range(0, len(price_grouped)):
        name = price_grouped.loc[i,'coinname']+':'+price_grouped.loc[i,'exchange']
        if name in d:
            j = d[name] + 1
            if j >= 0 and j < len(v):
                u[j]=price_grouped.loc[i,'price']
            else:
                print("Warning: invalid index " + str(j) + " for '" + name + "'")
        else: 
             print("not found the '" + name + "'")    

with open("big_data.csv", 'a') as fout:
    fout.write(str(v)[1:-1] + '\n')

with open("price.csv", 'a') as f:
    f.write(str(u)[1:-1] + '\n')