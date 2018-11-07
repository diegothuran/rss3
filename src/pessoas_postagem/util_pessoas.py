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
        if(article.date_publish == None):
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


# def format_date(raw_date):
#     formated_date = datetime.datetime.strptime(raw_date, '%d/%m/%Y %Hh%M%S').strftime("%Y-%m-%d %H:%M:%S")
#     return formated_date
# 
# def news_from_link(ref_link, news_from_globo):
#     row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
#     
#     article = NewsPlease.from_url(ref_link)
#     if (article is not None):
#         # Data returned by the NewsPlease
#         row['titulos'].append(article.title)
#         row['noticia'].append(article.text)
#         row['abstract'].append(article.text)
#         row['links'].append(article.url)
#         
#         if(news_from_globo):
#             # we need to get the date from the original url, the date returned by the NewsPlease is wrong
#             page_time = urllib.request.urlopen(article.url)
#             soup_date = BeautifulSoup(page_time, 'html.parser')
#             time_tag = soup_date.find_all('time', attrs={'itemprop': 'datePublished'})
#             public_date = time_tag[0].text 
#             formated_date = format_globo_date(public_date)
#             row['date'].append(formated_date)
#         else:
#             formated_date = str(article.date_publish)
#             row['date'].append(formated_date)
#         
#         path_image = article.image_url
#          
#         if path_image == '' or path_image == None:
#             row['image'].append(0)
#         else:
#             row['image'].append(download_and_move_image(article.image_url))
#           
#         news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
#         
#         print(news.date[0])
#         try:
#             print(row['titulos'])
#             news_in_db = pessoas_table.check_news(news)
#             print('news_in_db: ' + str(news_in_db))
#                
#             if(not news_in_db):
#                 row = pd.DataFrame(row)
#                 df, categories = pessoas_lexical.lexical_corpus_and_title(row)
#                 print(categories)
#                    
#                 # DB categories and image
#                 if(categories != [set()]):
#                     news.set_categories(categories)
#                     pessoas_table.save_news(news)
#                     pessoas_post.post_news(df)
#                        
#         except:
#             print('Empty News')
        
        