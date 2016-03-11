# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:52:36 2016

@author: Rohan Kulkarni
"""
import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.tsa.stattools as stat_tools
import statsmodels.tsa.tsatools as tsa_tools
import statsmodels.api as sm
import stock_headlines as news
import sys
alchemypath = os.path.dirname(os.path.abspath(__file__))+"/alchemyapi_python"
sys.path.append(alchemypath)
import alchemy_api as alchemy

def calculateSentimentOnNews(ticker,predictions):
    headlines = news.getHeadlines(ticker)
    overallSentimentScore = 0
    for h in headlines:
        res = alchemy.getSentiment(h)
        if res['status'] == 'OK':
            sentiment = res['docSentiment']
            if sentiment['type'] != 'neutral':
                overallSentimentScore += float(sentiment['score'])
    predictions = [each + overallSentimentScore/10 for each in predictions]
    return predictions
    
def main():
    tickers = ['BAC','C','IBM','AAPL','GE','T','MCD','NKE','TWTR','TSLA']
    curDir =   os.path.dirname(os.path.abspath(__file__))
    
    for ticker in tickers:
        data = pickle.load(open(curDir+'/historical_stock_data/'+ticker+'parsed.pickle', "rb" )) 
        ts = np.asarray([float(each[1]) for each in data['stocks']])
        res = sm.tsa.arma_order_select_ic(ts, ic=['aic', 'bic'],trend='c')
        p,q = res.aic_min_order[0],res.aic_min_order[1]
        model = sm.tsa.ARMA(ts,(p,q)).fit()
        predictions = model.predict(len(ts),len(ts)+1)
        adjustedPredictions = calculateSentimentOnNews(ticker,predictions)
        final = np.concatenate((ts,adjustedPredictions),axis=0)
       
        print "Prediction for stock ticker : " + ticker
        print final[-1]
        '''
        plt.plot(final,'b')
        plt.show()
        '''
if __name__=='__main__':
    main()