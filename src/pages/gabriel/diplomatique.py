# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

def get_urls():
    try:
        urls = [] 
        link = 'https://diplomatique.org.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='owl-carousel')
        for div in noticias[1:]:
            try:
                href = div.find_all('a', href=True)[0]['href']
                urls.append(href)
            except:
                pass
        
        return urls
    except:
        raise Exception('Exception in diplomatique')
