
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

import Database.seguranca_table as seguranca_table
import Database.credito_table as credito_table 
import Database.varejo_table as varejo_table
import Database.midia_table as midia_table  
  
import time

from lexical_analyzer_package import seguranca_lexical, varejo_lexical, credito_lexical, midia_lexical

def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, ' %d/%m/%Y %Hh%M ').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date


link = 'https://g1.globo.com/economia/pme/pequenas-empresas-grandes-negocios/'
print('url_globo: ' + str(link))

page = urllib.request.urlopen(link)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

news = soup.find_all('div', class_='feed-post bstn-item-shape type-materia')
for new in news:
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    
    internal_link = new.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover', href=True)
    ref = internal_link[0]['href']
    article = NewsPlease.from_url(ref)
#     abstract = article.description
#     print(abstract)
    
    # Data returned by the NewsPlease
    titulo = article.title
    noticia = article.text
    image_url = None
    image_url = article.image_url
    news_url = article.url
    
    # we need to get the date from the original url, the date returned by the NewsPlease is wrong
    page_time = urllib.request.urlopen(news_url)
    soup_date = BeautifulSoup(page_time, 'html.parser')
    time_tag = soup_date.find_all('time', attrs={'itemprop': 'datePublished'})
    public_date = time_tag[0].text 
    formated_date = format_date(public_date)
    
    row['titulos'].append(titulo)
    row['links'].append(news_url)
    row['date'].append(formated_date)
    row['noticia'].append(noticia)
    row['abstract'].append(noticia)
    if(image_url is not None):
        path_image = image_url
        row['image'].append(download_and_move_image(path_image))
    else:
        row['image'].append(0)
        
    news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])

    print('\n --- Seguranca ---')
    try:
        print(titulo)
        news_in_db = seguranca_table.check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = seguranca_lexical.lexical_corpus_and_title(row)
            print(categories)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
                seguranca_table.save_news(news)
#                 post_news(df)
    except:
        print('Empty News')
    
    print('\n --- Credito ---')
    try:
        print(titulo)
        news_in_db = credito_table.check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = credito_lexical.lexical_corpus_and_title(row)
            print(categories)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
#                 credito_table.save_news(news)
#                 post_news(df)
    except:
        print('Empty News')
        

    print('\n --- Varejo ---')
    try:
        print(titulo)
        news_in_db = varejo_table.check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = varejo_lexical.lexical_corpus_and_title(row)
            print(categories)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
#                 varejo_table.save_news(news)
#                 post_news(df)
    except:
        print('Empty News')
    
    
    print('\n --- Midia ---')
    try:
        print(titulo)
        news_in_db = midia_table.check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = midia_lexical.lexical_corpus_and_title(row)
            print(categories)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
                midia_table.save_news(news)
#                 post_news(df)
    except:
        print('Empty News')   
