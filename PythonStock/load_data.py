# Loading data from data provider

import tushare as ts

df = ts.get_realtime_quotes('sh') #Single stock symbol

print df