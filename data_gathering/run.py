from data_gathering import *
import os
import json

stock_name = "BAJAJ-AUTO.NS"
path = ""

if not os.path.exists('data'):
    os.makedirs('data')

path = "../data/{}".format(stock_name)

if not os.path.exists(path):
    os.makedirs(path)
    
## fetch historical data

hist = HistoricalData(stock_name, from_date = [2018,1,1], to_date=[2018,5,30], path = path)
hist.create_csv()
hist.info_plot('Open', 'Close')

## figures

price = hist.get_close()
emd = EMD(price, path=path)
emd.save_figure('{}-trend'.format(stock_name), type='trend')
emd.save_figure('{}-ds'.format(stock_name), type='ds')

## calc standard deviation
sd = hist.standard_deviation('Open')
with open("{}/sd.json".format(path), 'w') as outfile:
    json.dump(sd, outfile)
    
## get recent news

news = News("Finance", path = path)
news.export_json()