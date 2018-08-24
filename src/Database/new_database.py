#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from Model import News
from Database import connection
import datetime
from dateutil import parser
import postagem.Util as Util


def save_news(news=News):
    cnx = connection.connection()

    try:
        cursor = cnx.cursor()
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         now = datetime.datetime(2009, 5, 5)
#         str_now = now.date().isoformat()
        str_now = datetime.datetime.now().strftime("%Y-%m-%d")
        
        cats = Util.join_categories(news.categories[0])
        add_news = ("INSERT INTO noticias "
                    "(id, abstract, noticia, public_date, image, titulo, link, cheated_at, categories) "
                        "VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)", (news.abstract[0], news.news[0],
                                                                                   news.date[0], news.media[0],
                                                                                news.title[0], news.link[0], str_now, cats))

        cursor.execute(*add_news)
    except Exception as e:
        print(e)

    cnx.close()


def select_news(news =News):
    cnx = connection.connection()
    try:
        cursor = cnx.cursor()
        news.date[0] = parser.parse(news.date[0])
        query = ("SELECT * FROM noticias WHERE abstract= %s and titulo = %s", (news.abstract[0],
                                                                            news.title[0]))
        result = cursor.execute(*query)
        cnx.close()

        return result
    except Exception as e:
        print(e)

def check_news(news =News):
    cnx = connection.connection()
    
    cursor = cnx.cursor()

    sql = "SELECT * FROM noticias WHERE titulo = %s"
    titulo = (news.title[0], )    
    cursor.execute(sql, titulo)
 
    rows = cursor.fetchall()
    if(len(rows) > 0):
        news_in_db = True
    else:
        news_in_db = False
    
    cnx.close()
    return news_in_db
