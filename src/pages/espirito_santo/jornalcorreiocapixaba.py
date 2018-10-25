# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


def get_urls():
    try:
        urls = [] 
        for i in range(10):
            link = 'http://jornalcorreiocapixaba.com.br/pt-BR/publicacoes/?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='block_topic_post_feature')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('article', class_='block_news_post')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalcorreiocapixaba')
