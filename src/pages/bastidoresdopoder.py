# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 7426845
RANK_BRAZIL = None
NAME = 'bastidoresdopoder'

def get_urls():
    try:  
        urls = []  
        for i in range(1,10):
            if(i == 1):
                link = 'http://www.bastidoresdopoder.com.br/'
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-post-content')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-1')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-2')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-3')
            else:
                link = 'http://www.bastidoresdopoder.com.br/page/' + str(i)
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-post-content')
            
            for noticia in noticias:
    #             print(noticia.find_all('a', href=True)[0]['href'])
                urls.append(noticia.find_all('a', href=True)[0]['href'])
        return urls
    except:
        raise Exception('Exception in bastidoresdopoder')
