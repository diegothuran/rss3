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

# def format_globo_date(raw_date):
#     formated_date = datetime.datetime.strptime(raw_date, ' %d/%m/%Y %Hh%M ').strftime("%Y-%m-%d %H:%M:%S")
#     return formated_date

def news_from_link(ref_link):
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    article = NewsPlease.from_url(ref_link)
    if (article is not None):
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['links'].append(article.url)
        row['abstract'].append(article.text)
#         if(article.date_publish == None):
        if((article.date_publish == None) or (article.date_publish > datetime.datetime.now())):
            row['date'].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            row['date'].append(article.date_publish)
        path_image = article.image_url
        print(path_image)
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
