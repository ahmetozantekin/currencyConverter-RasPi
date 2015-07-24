#!/usr/bin/env python

"""
Yahoo Finance API kullanarak paranın degerini anlik olarak gösterebilen
RaspberryPi üzerinde çalışan bir uygulama geliştirmesi.

finance.yahoo.com'un, http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={?}{?}=X
url'sini kullanacagiz.
"""

import urllib2
import xml.dom from minidom


URL = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={FROM}{TO}=X'

def para_degeri(url):
    # request -> response
    request = urllib2.Request(url)
    
    try:
        response = urllib2.urlopen(request)
        
    except urllib2.URLError: ## URL hatalı ise hiç bir şey yapmasın.
        return None
    
    sonuc = response.read()
    return sonuc


def cevir(FROM, TO, kacPARA):
    if FROM.lower() == TO.lower():
        return "Farklı para birimleri giriniz."
    
    data = para_degeri(URL.format(FROM, TO))
    #URL'de FROM ve TO yazan yerlere fonksiyonun parametrelerini yerlestirir
    
    if data:
        parcala = data.split(',')
        """
        URL cikti olarak 'USDTRY=X, 2.7410, "7/24/2015", "8:08am"'
        gibi bir cikti veriyor. Bunu virgüllerine gore parcalayıp
        dizinin 1. elemanini alirsak, paranin degerini elde ederiz.
        """
        
        try:
            return kacPARA + FROM + parcala[1]*kacPARA + TO
            #Örnek:   5      USD       2,74*5=13,5       TRY
            
        except (IndexError, ValueError):
            return "Yanlis para birimi girisi."
        

##TEST

print "Para Birimleri: USD, GBP, JPY, TRY, EUR, AUD, INR ..."
    
_from = input("Degeri cevrilecek para:(FROM) ")
_to   = input("Degere uyarlanacak para: (TO) ")
_para = input("kac para cevrilecek: ")
    
cevir(_from, _to, _para)