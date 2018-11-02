# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import pandas as pd
import urllib
import datetime

from newsplease import NewsPlease
from bs4 import BeautifulSoup

from Model.News import News
from postagem.Util import download_and_move_image 

from Database import pessoas_table
from lexical_analyzer_package import pessoas_lexical
from pessoas_postagem import pessoas_post
import requests

from Util import util


print("---------------------------------- UOL --------------------------------")
limit_links = 50
start_url = 'https://noticias.uol.com.br/politica/eleicoes/ultimas/'
lista_links = []
limite_links = 50
for j in range(1, int(limite_links / 10) + 1):
    lista_links.append(start_url + "#?next=0001H1294U" + str(30 * j) + "N")

    # Recupera o código fonte da URL
    fonte = requests.get(start_url)
    fonte_bs = BeautifulSoup(fonte.text)
    # Para o componente com a classe widget-news-list recupere todas as tags 'a' cujo conteúdo 'href' seja um endereço http válido
    links_coletados = fonte_bs.find('div', class_='itens-indice').find_all('span', class_='titulo', limit=None)
    links_links = fonte_bs.find('div', class_='itens-indice').find_all('a')

    # Para cada link recuperado
    for titulo, link in zip(links_coletados, links_links):
        try:
            row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
            page = link.get('href')
            print(page)
            article = NewsPlease.from_url(page)
            row['titulos'].append(article.title)
            row['noticia'].append(article.text)
            news_url = article.url 
            row['links'].append(news_url)
            row['abstract'].append(article.text)
        #         row['date'].append(article.date_publish)
            formated_date = util.format_date(article.date_publish, news_url)
            print(formated_date)
            row['date'].append(formated_date)
                
            # image
            path_image = article.image_url
            if path_image == '' or path_image == None:
                row['image'].append(0)
            else:
                row['image'].append(download_and_move_image(article.image_url))
                     
            news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
            try:
                print(row['titulos'])
                news_in_db = pessoas_table.check_news(news)
                print('news_in_db: ' + str(news_in_db))
                if (not news_in_db):
                    row = pd.DataFrame(row)
                    df, categories = pessoas_lexical.lexical_corpus_and_title(row)
                    # DB categories
                    if (categories != [set()]):
                        news.set_categories(categories)
                        pessoas_table.save_news(news)
                        pessoas_post.post_news(df)
            except:
                print('Empty News')
        except:
            print('uol : error on NewsPlease')

