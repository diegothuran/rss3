# coding: utf-8

import sys
sys.path.insert(0, '../../src')
import feedparser
import pandas as pd

import urllib

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from postagem.lexical_analyzer import lexical
from postagem.site_wordpress import post_news
from Model.News import News
from Database.new_database import save_news, check_news

from newsplease import NewsPlease
from bs4 import BeautifulSoup
import requests

import datetime

''' com a folha '''
# hit_list = ["https://www.jornaldocomercio.com/_conteudo/politica/rss.xml",
#            "http://pox.globo.com/rss/g1/politica/", "https://feeds.folha.uol.com.br/poder/rss091.xml"]

''' sem a folha '''
hit_list = ["https://www.jornaldocomercio.com/_conteudo/politica/rss.xml", "http://pox.globo.com/rss/g1/politica/"]

''' uol '''
# hit_list = ["http://rss.uol.com.br/feed/noticias.xml"]

future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]


# In[3]:
entries = []
for feed in future_calls:
    entries.extend(feed["items"])


resultados = pd.DataFrame({'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []})


def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, '%a, %d %b %Y %H:%M:%S %z').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date


i = 0
for entrie in entries:
    i+=1
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    domain = extract_domain(entrie['link'])
    path_image = ""
 
    '''
    if  domain == 'globo':
        row['titulos'].append(entrie['title'])
        row['links'].append(entrie['link'])
        formated_date = format_date(entrie['published'])
        row['date'].append(formated_date)
        row['noticia'].append(entrie['summary_detail']['value'])
        row['abstract'].append(entrie['summary_detail']['value'])
        if 'media_content' in entrie:
            path_image = entrie['media_content'][0]['url']
            row['image'].append(download_and_move_image(path_image))
        else:
            row['image'].append(0)
    '''
    if domain == 'jornaldocomercio':
        row['titulos'].append(entrie['title'])
        row['links'].append(entrie['link'])
        formated_date = format_date(entrie['published'])
        row['date'].append(formated_date)
        row['abstract'].append(entrie['summary'])
        noticia = get_noticia_comercio(entrie['link'])
        row['noticia'].append(noticia)
        if 'media_content' in entrie:
            path_image = entrie['media_url']
            if path_image != '':
                row['image'].append(download_and_move_image(path_image))
            else:
                row['image'].append(0)
        else:
            row['image'].append(0)
 
    news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
 
    try:
        print(row['titulos'])
        news_in_db = check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = lexical(row)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
                save_news(news)
                post_news(df)
    except:
        print('Empty News')



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
        row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
        article = NewsPlease.from_url(link.get('href'))
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        news_url = article.url 
        row['links'].append(news_url)
        row['abstract'].append(article.text)
    #         row['date'].append(article.date_publish)

        try:
            if('ne10' in news_url):
                # we need to get the date from the original url, the date returned by the NewsPlease is wrong
                page_time = urllib.request.urlopen(news_url)
                soup_date = BeautifulSoup(page_time, 'html.parser')
                time = soup_date.find_all('p', attrs={'class': 'data-materia'})
                raw_date = time[0].text 
                raw_date = raw_date.replace(',', '')
                raw_date = raw_date.split()
                public_date = raw_date[2] + ' ' + raw_date[4]
                formated_date = datetime.datetime.strptime(public_date, '%d/%m/%Y %Hh%M').strftime("%Y-%m-%d %H:%M:%S")
                row['date'].append(formated_date)
            elif('band' in news_url):
                # we need to get the date from the original url, the date returned by the NewsPlease is wrong
                page_time = urllib.request.urlopen(news_url)
                soup_date = BeautifulSoup(page_time, 'html.parser')
                time = soup_date.find_all('meta', attrs={'itemprop': 'datePublished'})
                raw_date = time[0].text 
                raw_date = raw_date.split()
                public_date = raw_date[0] + ' ' + raw_date[2]
                formated_date = datetime.datetime.strptime(public_date, '%d/%m/%Y %H:%M').strftime("%Y-%m-%d %H:%M:%S")
                row['date'].append(formated_date)
            elif('folha' in news_url):
                # we need to get the date from the original url, the date returned by the NewsPlease is wrong
                page_time = urllib.request.urlopen(news_url)
                soup_date = BeautifulSoup(page_time, 'html.parser')
                time = soup_date.find_all('time', attrs={'class': 'c-more-options__published-date'})
                formated_date = time[0]['datetime']
                row['date'].append(formated_date)          
            elif('congressoemfoco' in news_url):
                print(' --- congressoemfoco --- ')
                # we need to get the date from the original url, the date returned by the NewsPlease is wrong
                page_time = urllib.request.urlopen(news_url)
                soup_date = BeautifulSoup(page_time, 'html.parser')
                time = soup_date.find_all('time', attrs={'class': 'post-published updated'})
                public_date = time[0]['datetime']
                formated_date = datetime.datetime.strptime(public_date, '%Y-%m-%dT%H:%M:%S+00:00').strftime("%Y-%m-%d %H:%M:%S")
                row['date'].append(formated_date)
    
            # if no case is caught: This happens in the case of the 'noticias.uol.com.br' page
            else:
                print(' --- noticias.uol.com.br ---')
                # we need to get the date from the original url, the date returned by the NewsPlease is wrong
                # The BeautifulSoup cannot get the actual date of the news, so I'll set the time now.
                formated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                row['date'].append(formated_date)
        except:
            formated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            news_in_db = check_news(news)
            print('news_in_db: ' + str(news_in_db))
            if(not news_in_db):
                row = pd.DataFrame(row)
                df, categories = lexical(row)
                # DB categories
                if(categories != [set()]):
                    news.set_categories(categories)
                    save_news(news)
                    post_news(df)
        except:
            print('Empty News')

