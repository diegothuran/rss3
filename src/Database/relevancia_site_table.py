#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../src')
from Model import Relevancia_Site
from Database import connection
import datetime
from dateutil import parser
import postagem.Util as Util


def save(relevancia_site = Relevancia_Site):
    cnx = connection.connection()

    try:
        cursor = cnx.cursor()
        
        add_news = ("INSERT INTO relevancia_site "
                    "(id, site, relevancia) "
                        "VALUES (NULL, %s, %s)", (relevancia_site.site[0], relevancia_site.relevancia[0]))

        cursor.execute(*add_news)
    except Exception as e:
        print(e)

    cnx.close()


def select(relevancia_site = Relevancia_Site):
    cnx = connection.connection()
    try:
        cursor = cnx.cursor()
        query = ("SELECT * FROM relevancia_site WHERE site = %s", (relevancia_site.site[0]))
        result = cursor.execute(*query)
        cnx.close()
 
        return result
    except Exception as e:
        print(e)
 
def check(relevancia_site = Relevancia_Site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
 
    sql = "SELECT * FROM relevancia_site WHERE site = %s"
    site = (relevancia_site.site[0], )    
    cursor.execute(sql, site)
  
    rows = cursor.fetchall()
    if(len(rows) > 0):
        site_in_db = True
    else:
        site_in_db = False
     
    cnx.close()
    return site_in_db

def update(relevancia_site = Relevancia_Site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
    sql = "UPDATE relevancia_site SET relevancia = %s WHERE site = %s"
    site = (relevancia_site.relevancia[0], relevancia_site.site[0],)    
    cursor.execute(sql, site)
    
    cnx.close()
    