import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as dates

df=pd.read_csv('big_data.csv')
coin_list = ['bitcoin', 'ethereum', 'monero', 'stellar', '0x']


#找出交易量前几的交易所
def findmost(coinname, rank=5):
    df3 = df.filter(regex='^%s:' % coinname)
    l=[] 
    for column in df3:
        m=df3[column].mean()
        l.append((column,m))

    s=sorted(l, key=lambda l: l[1],reverse=True) 
    return([x[0] for x in s[0:rank]])



#画图呈现交易量的前五
def draw(plotname, coinname, filename):
    times=df.iloc[:,0]
    print(a)
    result = pd.concat([times,df[a]],axis=1)
    result['Time Stamp'] = pd.to_datetime(result['Time Stamp'], format="'%Y-%m-%d %H:%M:%S'")
    result.plot(x='Time Stamp')
    plt.xlabel('time')
    plt.ylabel(plotname + ' in 24 hours')
    plt.xticks( rotation=25, ha="right")
    ax = plt.gca()
    labels = []
    ax.set_xticklabels(labels)
    plt.title(coinname + ' exchange volume')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('figs/' + coinname + '_' + filename + '_all.png')
    # plt.show()

tasks = [['big_data.csv', 'Exchange Volume', 'vol'], ['price.csv', 'Price', 'price']]
for task in tasks:
    df = pd.read_csv(task[0])
    df3
    for s in coin_list:
        a=findmost(s,5)
        draw(task[1], s, task[2])

