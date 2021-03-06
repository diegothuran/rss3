# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 287
RANK_BRAZIL = None
NAME = 'buzzfeed.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.buzzfeed.com/badge/newsbr'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='xs-px05 sm-pl05')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in buzzfeed')
    
