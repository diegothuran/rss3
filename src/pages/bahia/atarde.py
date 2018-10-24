# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


def get_urls():
    try:
        urls = [] 
        root = 'http://atarde.uol.com.br'
        link = 'http://atarde.uol.com.br/ultimas-noticias'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='boxMateria')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href 
            print(full_link)
            urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in atarde')
