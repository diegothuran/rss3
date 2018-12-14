#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../src')
from Model import Relevancia_Site
from Database import connection
import datetime
from dateutil import parser
import postagem.Util as Util

from pandas import DataFrame


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

def select(site):
    cnx = connection.connection()
    cursor = cnx.cursor()
  
    sql = "SELECT * FROM relevancia_site WHERE site = %s"
    site = (site, )    
    cursor.execute(sql, site)
    result = cursor.fetchall()[0] 
    cnx.close()
    return result

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

def select_form_date(request_date):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas "
             "WHERE public_date = %s")
    
    str_date = request_date.strftime("%Y-%m-%d")
#     hire_start = datetime.date(1999, 1, 1)
#     hire_end = datetime.date(1999, 12, 31)
    str_date = (str_date, )    
    cursor.execute(query, str_date)
    rows = cursor.fetchall()
    print(len(rows))
    
    cursor.close()
    cnx.close()
    return len(rows)
    
def select_site_in_link(site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
#     query = ("SELECT * FROM pessoas WHERE id = %s AND link LIKE %s")
#     formated_string = '%' + site + '%'
#     request_site = ('1', formated_string, )    
    
    query = ("SELECT * FROM pessoas WHERE link LIKE %s")
    formated_string = '%' + site + '%'
    request_site = (formated_string, )    
    
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
def update_site(site):
    cnx = connection.connection()
    cursor = cnx.cursor()

    query = ("UPDATE pessoas SET site = %s WHERE link LIKE %s")
     
    formated_string = '%' + site + '%'
    val = (site, formated_string, )    
    cursor.execute(query, val)
    
    cnx.commit()

    print(cursor.rowcount, "record(s) affected") 
     
    cursor.close()
    cnx.close()
    
def select_site(site):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas WHERE site = %s")
    request_site = (site, )    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
def select_categories(categorie):
    cnx = connection.connection()     
    cursor = cnx.cursor()

    
    query = ("SELECT categories FROM pessoas WHERE categories LIKE %s")
    formated_string = '%' + categorie + '%'
    request_site = (formated_string, )    
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    

def select_site_pd(site):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas WHERE site = %s")
    request_site = (site, )    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
    print(len(rows))
    for row in rows:
        print(row)
    df = DataFrame(rows)
#     print(df)
#     df.columns = rows.keys()
    
#     print(df.iloc[:,8])
    cursor.close()
    cnx.close()
    
    categories = df.iloc[:,8]
    return categories


def get_interval(data_inicial, data_final):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas "
             "WHERE public_date BETWEEN %s AND %s")
    
#     str_data_inicial = data_inicial.strftime("%Y-%m-%d")
#     str_data_final = data_final.strftime("%Y-%m-%d")
    request_site = (data_inicial, data_final, )    
    cursor.execute(query, request_site)
    
    rows = cursor.fetchall()
    print(len(rows))
    print('aqui')
    for i in rows:
        print(i)
    
#     for (first_name, last_name, hire_date) in cursor:
#         print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))
    
    cursor.close()
    cnx.close()
    
    
    