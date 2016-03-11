# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 00:54:51 2016

@author: rohan
"""
from yahoo_finance import Share
import pickle
import os

def main():
    tickers = ['BAC','C','IBM','AAPL','GE','T','MCD','NKE','TWTR','TSLA']
    curDir =   os.path.dirname(os.path.abspath(__file__))
    for ticker in tickers:    
        stockHandle = Share(ticker)
        data = stockHandle.get_historical('2013-03-08', '2016-03-11')
        pickle.dump(data,open( curDir+'/historical_stock_data/'+ticker+'.pickle', "wb" ))
        print 'done'
    
    for ticker in tickers:
        d = {'stocks':[]}            
        data = pickle.load(open(curDir+'/historical_stock_data/'+ticker+'.pickle', "rb" )) 
        for each in data[::-1]:
            d['stocks'].append([each['Date'],each['Open']])
        pickle.dump(d,open( curDir+'/historical_stock_data/'+ticker+'parsed.pickle', "wb" ))
    print pickle.load(open( curDir+'/historical_stock_data/'+'AAPL'+'parsed.pickle', "rb" ))
    
if __name__=='__main__':
    main()