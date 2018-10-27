# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

def get_urls():
    try:
        urls = [] 
        root = 'https://www.acritica.com'
        link = 'https://www.acritica.com/channels/manaus'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='news-snippet highlight main with-links ')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href
#             print(full_link)
            urls.append(full_link)
            
        list_href = BeautifulSoup(req.text, "html.parser").find_all('a', class_='news-snippet highlight ')
         
        
        for i in range(len(list_href)):
            href = list_href[i]['href']
            full_link = root + href
#             print(full_link)
            urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in diariodoamazonas')
