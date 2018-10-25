# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests


def get_urls():
    try:
        urls = [] 
        link = 'https://apublica.org/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='mb-3')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h4', class_='mb-1')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h4', class_='card-title')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(ref_link)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in apublica')
    