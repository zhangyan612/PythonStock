import data_access as db
import pandas as pd
import datetime
import KDJ_Indicator

# Testing Database access code
shdaily = db.mongo_connect('test_database', 'indexdata')
if shdaily.count() > 0:
    print 'Database Connected'

# Put the first dataset in

# List the data 
# initialize Values
K1 = 50
D1 = 50

# for each day, calculate data and insert into db
for d in shdaily.find()[:10]:
    date = d['date']
    datalist = pd.DataFrame(list(shdaily.find({'date':{"$lte": date}}).sort('date', -1)))
    data = datalist[:9] # get last 9 day data
    
    #if data.ix[1]['KDJ_K'] is not None:
    #    # get previous KDJ data from database
    #    K1 = data.ix[1]['KDJ_K']
    #    D1 = data.ix[1]['KDJ_D']
    
    high = data['high'].values
    low  = data['low'].values
    close = data[:1]['close'].values
    K1,D1,K2,D2,J2 = KDJ_Indicator.KDJCalculation(K1,D1,max(high),min(low),close)
    d['KDJ_K'] = K2[0]
    d['KDJ_D'] = D2[0]
    d['KDJ_J'] = J2[0]
    K1 = K2
    D1 = D2
    db.kdj_insert('test_database', 'ShKDJ', d)
    #print d



