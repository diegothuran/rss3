# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

def get_urls():
    try:
        urls = [] 
        link = 'https://nocaute.blog.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='jet-smart-listing__post-title post-title-simple')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in nocaute')
    
