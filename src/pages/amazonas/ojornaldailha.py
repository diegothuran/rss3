# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

def get_urls():
    try:
        urls = [] 
        for i in range(1, 10):
            if(i == 1):
                link = 'https://ojornaldailha.com/noticias/'
            else:
                link = 'https://ojornaldailha.com/noticias/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title td-module-title')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in diariodocentrodomundo')
