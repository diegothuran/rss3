# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

def get_urls():
    try:
        urls = []
        for i in range(1,10):
            if(i == 1):
                link = 'http://tribunadosertao.com.br/noticias/'
            else:
                link = 'http://tribunadosertao.com.br/noticias/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='post-title')
            for noticia in noticias:
#                 print(noticia.find_all('a', href=True)[0]['href'])
                urls.append(noticia.find_all('a', href=True)[0]['href'])
        
        return urls
    except:
        raise Exception('Exception in tribunadosertao')
