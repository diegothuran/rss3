# coding: utf-8

import sys
sys.path.insert(0, '../../src')
import feedparser
import pandas as pd

import urllib

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from lexical_analyzer_package import midia_lexical
from midia_postagem import midia_post
from Model.Social_News import Social_News
from Database import midia_table

from newsplease import NewsPlease
from bs4 import BeautifulSoup
import requests

import datetime

from Util import util

def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, '%d/%m/%Y %Hh%M%S').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date

def social_news_from_link(ref_link):
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': [], 
           'Pinterest': [], 'fb_comment': [], 'fb_share': [], 'fb_reaction': [], 'fb_total': []}
    
    article = NewsPlease.from_url(ref_link)
    if (article is not None):
        # Data returned by the NewsPlease
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['links'].append(article.url)
        row['abstract'].append(article.text)
        formated_date = str(article.date_publish)
        row['date'].append(formated_date)
        path_image = article.image_url
        if path_image == '' or path_image == None:
            row['image'].append(0)
        else:
            row['image'].append(download_and_move_image(article.image_url))
        
        Pinterest, fb_comment, fb_share, fb_reaction, fb_total = util.get_sharedcount_info(article.url)
        
        row['Pinterest'].append(Pinterest)
        row['fb_comment'].append(fb_comment)
        row['fb_share'].append(fb_share)
        row['fb_reaction'].append(fb_reaction)
        row['fb_total'].append(fb_total)
    
        social_news = Social_News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'],
                                  row['Pinterest'], row['fb_comment'], row['fb_share'], row['fb_reaction'], row['fb_total'])
        
        try:
            print(row['titulos'])
            news_in_db = midia_table.check_news(social_news)
            print('news_in_db: ' + str(news_in_db))
            
            if(not news_in_db):
                row = pd.DataFrame(row)
                df, categories = midia_lexical.lexical_corpus_and_title(row)
                
                # DB categories and image
                if(categories != [set()]):
                    social_news.set_categories(categories)
                    midia_table.save_news(social_news)
                    midia_post.post_news(df)
                    
        except:
            print('Empty News')
        
        