# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:02:06 2016

@author: rohan
"""
import stockretriever 

def getHeadlines(ticker):
    stocks = stockretriever
    news = stocks.get_news_feed(ticker)
    headlines = list()
    for each in news:
        headlines.append(each['title'])
    return headlines
    
if __name__=='__main__':
    getHeadlines()