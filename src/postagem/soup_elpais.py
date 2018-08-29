
# coding: utf-8
import sys
sys.path.insert(0, '../../src')
import urllib
from bs4 import BeautifulSoup
import requests
from newsplease import NewsPlease

import datetime
import pandas as pd

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from postagem.lexical_analyzer import lexical, lexical_soup_globo
from postagem.site_wordpress import post_news
from Model.News import News
from Database.new_database import save_news, check_news
import time

def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, ' %d/%m/%Y %Hh%M ').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date

link = 'https://brasil.elpais.com/tag/elecciones_brasil/a'
# for link in links:
print('url: ' + str(link))

page = urllib.request.urlopen(link)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# news = soup.find_all('div', class_='articulos articulos_cuerpo')
news = soup.find_all('div', class_='articulo__interior')
print(len(news))
i = 0
for new in news:
    print('\nindex : ' + str(i))
    i+=1
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    try:
        set_h2 = new.find_all('h2', class_='articulo-titulo')
        for h2 in set_h2:
            internal_link = new.find_all('a', href=True)
            ref = internal_link[0]['href']
        ref = 'https://brasil.elpais.com/' + str(ref)
        # NewsPlease
        article = NewsPlease.from_url(ref)

    except:
        try:
            internal_link = new.find_all('a', class_='enlace', href=True)
            if(internal_link == []):
                pass
            else:
                for temp in internal_link:
                    ref = temp['href']
                ref = 'https:' + str(ref)
                #NewsPlease
                article = NewsPlease.from_url(ref)
        except:
            article = None

    if(article is not None):
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['links'].append(article.url)
        row['abstract'].append(article.text)
        row['date'].append(article.date_publish)
        path_image = article.image_url
        if path_image == '' or path_image == None:
            row['image'].append(0)
        else:
            row['image'].append(download_and_move_image(article.image_url))
        news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
        try:
            print(row['titulos'])
            news_in_db = check_news(news)
            print('news_in_db: ' + str(news_in_db))
            if (not news_in_db):
                row = pd.DataFrame(row)
                df, categories = lexical(row)
                # DB categories
                news.set_categories(categories)
                save_news(news)
                post_news(df)
        except:
            print('Empty News')
        
