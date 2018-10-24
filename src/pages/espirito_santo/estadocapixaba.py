# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


def get_urls():
    try:
        urls = [] 
        link = 'http://estadocapixaba.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-12 news-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in estadocapixaba')
