
# coding: utf-8

# In[1]:


import feedparser
import pandas as pd
from postagem.Util import extract_domain, downlaod_and_move_image, get_noticia_comercio
from postagem.lexical_analyzer import lexical
from postagem.site_wordpress import post_news
from Model.News import News
from Database.new_database import save_news, check_news
from newsplease import NewsPlease

import datetime

# In[2]:
# hit_list = ["https://www.jornaldocomercio.com/_conteudo/politica/rss.xml",
#            "http://pox.globo.com/rss/g1/politica/mensalao/", "https://feeds.folha.uol.com.br/poder/rss091.xml"]

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
    entries.extend( feed[ "items" ] )


# In[4]:
resultados = pd.DataFrame({'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []})

def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, '%a, %d %b %Y %H:%M:%S %z').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date

# In[5]:
i = 0
for entrie in entries:
    i+=1
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    domain = extract_domain(entrie['link'])
    if  domain == 'globo':
        row['titulos'].append(entrie['title'])
        row['links'].append(entrie['link'])
        formated_date = format_date(entrie['published'])
        row['date'].append(formated_date)
        row['noticia'].append(entrie['summary_detail']['value'])
        row['abstract'].append(entrie['summary_detail']['value'])
        if 'media_content' in entrie:
            path_image = entrie['media_content'][0]['url']
            row['image'].append(downlaod_and_move_image(path_image))
        else:
            row['image'].append(0)

    elif domain == 'jornaldocomercio':
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
                row['image'].append(downlaod_and_move_image(path_image))
            else:
                row['image'].append(0)
        else:
            row['image'].append(0)
    elif domain == 'uol':
        link = entrie['link']
        article = NewsPlease.from_url(link)
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['links'].append(article.url)
        row['abstract'].append(article.text)
        row['date'].append(article.date_publish)
        path_image = article.image_url
        if path_image == '' or path_image == None:
            pass
        else:
            row['image'].append(downlaod_and_move_image(article.image_url))

    news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])

    try:
        print(row['titulos'])
        news_in_db = check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = lexical(row)
            # DB categories
            news.set_categories(categories)
            save_news(news)
            post_news(df)
    except:
        print('Empty News')

# # In[6]:
# resultados_cat = lexical(resultados)
#  
#  
# # In[7]:
# post_news(resultados_cat)

