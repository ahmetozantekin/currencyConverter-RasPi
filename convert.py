#!/usr/bin/env python

"""
finance.yahoo.com, http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={?}{?}=X

"""

import urllib2
import xml.dom from minidom


URL = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={FROM}{TO}=X'

def priceTag(url):
    # request -> response
    request = urllib2.Request(url)
    
    try:
        response = urllib2.urlopen(request)
        
    except urllib2.URLError: ## do nothing
        return None
    
    sonuc = response.read()
    return sonuc


def con(FROM, TO, MUCH):
    if FROM.lower() == TO.lower():
        return "Farklı para birimleri giriniz."
    
    data = priceTag(URL.format(FROM, TO))
    #URL ~> FROM ve TO 
    
    if data:
        S = data.split(',')
        """
        USDTRY=X, 2.7410, "7/24/2015", "8:08am"'
        """
        
        try:
            return MUCH + FROM + s[1]*kacPARA + TO
            #EXMP.:   5      USD       2,74*5=13,5       TRY
            
        except (IndexError, ValueError):
            return "Wrong Currency."
        

##TEST

print "Para Birimleri: USD, GBP, JPY, TRY, EUR, AUD, INR ..."
    
_from = input("FROM ")
_to   = input("TO ")
_para = input("MUCH: ")
    
con(_from, _to, _para)
