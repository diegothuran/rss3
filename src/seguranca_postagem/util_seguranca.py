# coding: utf-8

import sys
sys.path.insert(0, '../../src')
import feedparser
import pandas as pd

import urllib

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from lexical_analyzer_package import seguranca_lexical
from seguranca_postagem import seguranca_post
from Model.News import News
from Database import seguranca_table

from newsplease import NewsPlease
from bs4 import BeautifulSoup
import requests

import datetime

from Util import util


def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, '%d/%m/%Y %Hh%M%S').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date

def news_from_link(ref_link):
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    
    article = NewsPlease.from_url(ref_link)
    if (article is not None):
        # Data returned by the NewsPlease
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['abstract'].append(article.text)
        row['links'].append(article.url)
        formated_date = str(article.date_publish)
        row['date'].append(formated_date)
        path_image = article.image_url
         
        if path_image == '' or path_image == None:
            row['image'].append(0)
        else:
            row['image'].append(download_and_move_image(article.image_url))
          
        news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
          
        try:
            print(row['titulos'])
            news_in_db = seguranca_table.check_news(news)
            print('news_in_db: ' + str(news_in_db))
              
            if(not news_in_db):
                row = pd.DataFrame(row)
                df, categories = seguranca_lexical.lexical_corpus_and_title(row)
                print(categories)
                  
                # DB categories and image
                if(categories != [set()]):
                    news.set_categories(categories)
                    seguranca_table.save_news(news)
                    seguranca_post.post_news(df)
                      
        except:
            print('Empty News')
        
        