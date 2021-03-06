#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib3
import tldextract
import os
import wget
from bs4 import BeautifulSoup
import requests
from newsplease import NewsPlease
import pandas as pd
from selenium import webdriver
import shutil


def download_image(url, path_to_save_image):
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    with open(path_to_save_image, 'wb') as out:
        while True:
            data = r.read(15)
            if not data:
                break
            out.write(data)

    r.release_conn()


def extract_domain(link):
    ext = tldextract.extract(link)
    return ext.domain

def download_and_move_image(path_to_image):
    root_path = os.getcwd()
    try:
        file_name = wget.download(path_to_image)
        print(file_name)
        dst = os.path.join(os.getcwd(), 'images', file_name)
        print(dst)
        shutil.move(os.path.join(root_path, file_name), dst)
    except Exception as e:
        print(e)
        dst = '0'
    return dst

# def download_and_move_image(path_to_image):
#     file_name = wget.download(path_to_image)
# #     destination = os.path.join('/home/diego/Documentos/rss_reader/Untitled Folder/Images', file_name)
#     destination = os.path.join('../Data/download', file_name)
#     os.rename(file_name, destination)
# #     print(file_name)
#     return file_name

# def download_and_move_image(path_to_image):
#     files_in_image_folder = os.listdir('../Data/download')
#     file_name = wget.download(path_to_image)
#     if file_name in files_in_image_folder:
#         temp = file_name.split('.')
#         temp[0] = temp[0] + '2'
#         temp = clean_join_strings(temp)
#         os.rename(file_name, temp)
#         file_name = temp
#         del temp
#         destination = os.path.join('../Data/download', file_name)
#         os.rename(file_name, destination)
#     else:
#         destination = os.path.join('../Data/download', file_name)
#         os.rename(file_name, destination)
#     return file_name

def get_noticia_uol(link):
    req = requests.get(link)
    bs = BeautifulSoup(req.text).find('div', id='texto').find_all('p')
    images = BeautifulSoup(req.text).find('div', id='texto').find_all('img')
    link_image = ""
    noticia = []
    if bs == []:
        link_image = 0
        pass
    else:

        ext = tldextract.extract(link)
        domain = ext.domain
        subdomain = ext.subdomain
        if images == []:
            noticia = bs
            link_image = 0
        else:
            i = 0
            for p in bs:
                if i >= 2:
                    text = p.contents[0]
                    if isinstance(text, str):
                        noticia.append(p.contents[0])
                i += 1
            src = images[0].get('src')
            link_image = src

    return join_strings(noticia), link_image

def join_strings(list_of_strings):

    """
        Método para transformar tokens em uma única sentença
    :param list_of_strings: Lista com os tokens
    :return: sentença formada pela união dos tokens
    """
    return "<p>".join(list_of_strings)


def clean_join_strings(list_of_strings):

    """
        Método para transformar tokens em uma única sentença
    :param list_of_strings: Lista com os tokens
    :return: sentença formada pela união dos tokens
    """
    return "".join(list_of_strings)

def get_noticia_comercio(link):
    print(link)
    article = NewsPlease.from_url(link)
    #req = requests.get(link)

    #bs = BeautifulSoup(req.text).find('div', class_='noticia espacamento claro').find_all('div')
    #noticia = ""
    #for div in bs:
#   #      noticia += str(div.contents[0].encode('utf-8'))
    #    if len(div.contents) > 0:
    #        noticia += str(div.contents[0])

    return article.text

# def get_noticia_comercio(link):
#     req = requests.get(link)
#     bs = BeautifulSoup(req.text).find('div', class_='noticia espacamento claro').find_all('div')
#     noticia = ""
#     for div in bs:
# #         noticia += str(div.contents[0].encode('utf-8'))
#         if len(div.contents) > 0:
#             noticia += str(div.contents[0])
# 
#     return noticia

def join_categories(categories):
    str_categories = ', '.join(str(c) for c in categories)
    return str_categories

def categories_db_to_categories(categories_db):
    categories = categories_db.split(', ')
    return categories

def news_from_link(link):
    article = NewsPlease.from_url(link)
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    if (article is not None):
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['links'].append(article.url)
        row['abstract'].append(article.text)
        row['date'].append(article.date_publish)
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
            if (not news_in_db):
                row = pd.DataFrame(row)
                df, categories = lexical(row)
                # DB categories
                if (categories != [set()]):
                    news.set_categories(categories)
                    save_news(news)
                    post_news(df)
        except:
            print('Empty News')

