#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import requests
import json
import base64
import datetime
from time import gmtime, strftime
import string 
import numpy as np
import copy

USER = b'admxarx'
PASSWORD = b'!xarx@2018*'

URL = 'https://seguranca.xarx.rocks/wp-json/wp/v2'
# URL = 'https://varejo.xarx.rocks/wp-json/wp/v2'

token = base64.standard_b64encode(USER + b':' + PASSWORD)
headers = {b'Authorization': b'Basic ' + token}

# categoria sem_categoria : 1
# categoria geral : 97
INDEX_CATEGORIES = {'ac' : 38,
                    'al' : 28,
                    'ap' : 39,
                    'am' : 40,
                    'ba' : 29,
                    'ce' : 30,
                    'df' : 23,
                    'es' : 46,
                    'go' : 24,
                    'ma' : 31,
                    'mt' : 25,
                    'ms' : 26,
                    'mg' : 47,
                    'pa' : 41,
                    'pb' : 32,
                    'pr' : 51,
                    'pe' : 33,
                    'pi' : 34,
                    'rj' : 48,
                    'rn' : 35,
                    'rs' : 52,
                    'ro' : 42,
                    'rr' : 43,
                    'sc' : 53,
                    'sp' : 49,
                    'se' : 36,
                    'to' : 44,
    
                    'jungmann' : 8, 
                    'segurança pública' : 9, 
                    'susp' : 10, 
                    'depen' : 11, 
                    'senasp' : 12, 
                    'penitenciária' : 13, 
                    'intervenção' : 14, 
                    'defesa' : 15, 
                    'tráfico' : 16, 
                    'fronteira' : 17, 
                    'drogas' : 18, 
                    'prf' : 19, 
                    'pf' : 20,
                    
                    'violência' : 54, 
                    'assalto' : 55, 
                    'sequestro' : 56, 
                    'presídio' : 57, 
                    'preso' : 58,
                    'assassinato' : 59, 
                    'crime' : 60, 
                    'julgamento' : 61, 
                    'condenação' : 62, 
                    'fuga' : 63,
                    'ladrão' : 64,
                    'polícia' : 65
                    }


def remove_punctuation(input_text):
    """
    Removes the punctuation from the input_text string
    python 2 (string.maketrans) is different from python 3 (str.maketrans)
    
    Parameters
    ----------
    input_text: string in which the punctuation will be removed
    
    Return
    ------
        input_text without the puncutation
    """
    punct = string.punctuation
    trantab = str.maketrans(punct, len(punct) * ' ')  # Every punctuation symbol will be replaced by a space
    return input_text.translate(trantab)

def join_strings(list_of_strings):
    """
        Método para transformar tokens em uma única sentença
    :param list_of_strings: Lista com os tokens
    :return: sentença formada pela união dos tokens
    """
    return ", ".join(list_of_strings)

def get_categories_idx(categories_names):
    """
    Get the wordpress categories index from the list of strings
    
    Parameters
    ----------
    categories_names: list of strings containing the name of the categories
    
    Return:
    ------
        categories_idx: list of integers containing the index of the categories
    """
#     categories_noticias = df['categorias'].values.tolist()
    list_categories = list(categories_names)
    categories_idx = []
    for category in list_categories:
        category = remove_punctuation(category)
        if category in INDEX_CATEGORIES.keys():
            categories_idx.append(INDEX_CATEGORIES[category])
    return categories_idx  

def get_categories_all_noticias(df):
    """
    Get the list of categories (list of categories (str)) for all 'noticias' 
    
    Parameters
    ----------
    df : dataframe containing all the data
    
    Return:
    ------
        list_categorias: list of list of categories for all 'noticias'
    """
    categories_noticias = df['categorias']
    list_categories = []
    for categories_noticia in categories_noticias:
        list_categories.append(remove_punctuation(categories_noticia).split())
    return list_categories

def get_categorias_noticia(df, idx_noticia):
    """
    Get the categories (list of categories (str)) for 'noticia' at idx_noticia index 
    
    Parameters
    ----------
    df : dataframe containing all the data
    
    Return:
    ------
        list_categorias: lista de categorias para a noticia no indice idx_noticia
    """
    categories_noticias = df['categorias']
    list_categories = remove_punctuation(categories_noticias[idx_noticia]).split()
    return list_categories  

def get_reduced_news(news_text):
    """
    Get the reduced text (content) of the news in the in the POST format
    
    Parameters
    ----------
    news_text : initial text of the news (in the current format is the abstract text)
    
    Return:
    ------
        reduced_news: reduced text (content) of the news in the in the POST format
    """
    # get paragraph_tag
    paragraph_tag = '\n'
    tag_idxs = []
    for i, _ in enumerate(news_text):
        if news_text[i:i + len(paragraph_tag)] == paragraph_tag:
            tag_idxs.append(i)
            
    br_tag = '<br />'
    br_idxs = []
    for i, _ in enumerate(news_text):
        if news_text[i:i + len(br_tag)] == br_tag:
            br_idxs.append(i)
            
    img_tag = 'img'
    foto_tag = 'foto'
    globo_tag = 'globo'
    estadao_tag = 'estadão'
    g1_tag = 'g1'
    
    # No caso das noticias do globo    
    try:
        # No caso de as noticias nao virem com imagens
        if(img_tag not in news_text[:tag_idxs[0]]):
            reduced_size = int(len(news_text) / 5)
            reduced_news = news_text[:reduced_size]
        else:
#             # vai comecar a ver a partir da tag final da imagem
            index_after_img = (br_idxs[0] + len(br_tag))
            verification_text = news_text[index_after_img:tag_idxs[5]]
            
            if((globo_tag in verification_text.lower()) or (foto_tag in verification_text.lower()) 
               or (estadao_tag in verification_text.lower()) or (g1_tag in verification_text.lower())):
                paragraph_idx = 0
                for i in range(5, 0, -1):
                    temp = news_text[tag_idxs[i-1]:tag_idxs[i]]
                    if((globo_tag in temp.lower()) or (foto_tag in temp.lower())
                       or (estadao_tag in temp.lower()) or (g1_tag in temp.lower())):
                        paragraph_idx = i
                        break
                    
                # paragrafo vazio
                if(abs(tag_idxs[paragraph_idx + 1] - tag_idxs[paragraph_idx]) < 10):
                    paragraph_idx += 1
                main_content = news_text[tag_idxs[paragraph_idx]:]
                reduced_size = int(len(main_content) / 5)
                reduced_news = main_content[:reduced_size]
            else:
                reduced_size = int(len(verification_text) / 5)
                reduced_news = verification_text[:reduced_size]
    # No caso das noticias do jornal do comercio, que tem um abstract diferente do texto em si
    except:
        reduced_news = news_text

    # Remover '\n' duplicado
    # ver isso no linux: se no lugar do \r\n vai ser so \n (https://stackoverflow.com/questions/14606799/what-does-r-do-in-the-following-script)
    # Tem que deixar essa parte se nao o texto ser postado quebrado
    reduced_news = reduced_news.replace('\n\n\t \n\n', '<p>')
    reduced_news = reduced_news.replace('\n', '<p>')
    
    return reduced_news


def post_news(df):
    use_image = True
          
    for idx in range(len(df)):
        row = df.iloc[idx]
        # date now        
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_df = str(row['date'])
        #date_df = datetime.datetime.strptime(row['date'], '%a, %d %b %Y %H:%M:%S %z').strftime("%Y-%m-%d %H:%M:%S")
        
        if(date_df < date_now):
            date = date_df
        else:
            date = date_now
            
        # title for the post
        title = row['titulos']
        # the wordpress categories index for the 'noticia' at idx_noticia index 
        categories_names = row['categorias']
        categories = get_categories_idx(categories_names)
        cats = join_strings(np.array(categories).astype(str).tolist())
        
        # the text of the 'abstract' and the link
        # texto_sumarizado: por enquanto apenas em seguranca
        news = row['abstract']
        reduced_news = get_reduced_news(news)
        temp = '... <p>Leia a íntegra em: ' + '<a href=' + row['links'] +'> ' + row['links']  + '</a>'
        
#         texto_contagem = 'Informações relacionadas ao SharedCount : <br> &emsp; Compartilhamentos no Pinterest = ' + str(row['Pinterest']) + \
#             ' <br> &emsp; Total de atividades relacionadas ao Facebook = ' + str(row['fb_total']) + ' - sendo: <br> &emsp;&emsp; Compartilhamentos = ' + \
#             str(row['fb_share']) + ' <br> &emsp;&emsp; Comentários = ' + str(row['fb_comment']) + ' <br> &emsp;&emsp; Reações = ' + \
#             str(row['fb_reaction']) + ' <br><br>'
#         
#         content = texto_contagem + reduced_news + temp
        
        content = reduced_news + temp

        # if the row does not have category
        if(categories == []):
            cats = '1' # category sem categoria
           
        # url
        url = URL
#             url_pernambuco = 'https://politica.xarx.rocks/pe/wp-json/wp/v2'
           
#             payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; \
#             name=\"title\"\r\n\r\n{0}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: \
#             form-data; name=\"categories\"\r\n\r\n{1}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: \
#             form-data; name=\"content\"\r\n\r\n{2}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: \
#             form-data; name=\"status\"\r\n\r\npublish\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--".format(title, 
#                                                                                                           cats, 
#                                                                                                           content).encode("utf-8")
                                                                                                         
       
#         payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; \
#         name=\"title\"\r\n\r\n{0}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: \
#         form-data; name=\"categories\"\r\n\r\n{1}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: \
#         form-data; name=\"content\"\r\n\r\n{2}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: \
#         form-data; name=\"status\"\r\n\r\npublish\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--".format(title, 
#                                                                                                       cats, 
#                                                                                                       content)
#                                                                                                          
#         headers_postman = {
#             'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#             'authorization': "Basic YWRtcG9saXRpY2E6eGFyeEAyMDE4",
#             'cache-control': "no-cache",
#             'postman-token': "660515d7-2398-f142-2660-69ff2d5ef344"
#         }
#       
#         r = requests.post(url + '/posts', headers=headers_postman, data=payload)
#         print('POST = ' + str(r))

        post = {'date': date,
                'title': title,
                'categories': cats,
                'content': content,
                'status': 'publish',
                }
                        
        r = requests.post(url + '/posts', headers=headers, json=post)
        print('POST = ' + str(r))
                             
        if(use_image): 
            try:
#                 image_path = '../Data/download/' + row['image'].encode('utf-8')
                image_path = row['image']
                media = {'file': open(image_path,'rb'), 'caption': 'picture'}
                image = requests.post(url + '/media', headers=headers, files=media)  
                print('IMAGE_POST = ' + str(image))      
                          
#                 # Como estava
#                 img_id = requests.get(url + '/media').json()[0]['id']
#                 post_id = requests.get(url + '/posts').json()[0]['id']
# #                 print(img_id)
# #                 print(post_id)
                   
                # Testa essa nova forma para ver se funciona
                img_id = (json.loads(image.content))['id']
                post_id = (json.loads(r.content))['id']
                print(img_id)
                print(post_id)
                              
                updated_post = {'featured_media' : img_id}
                               
                update = requests.post(url + '/posts/' + str(post_id), headers=headers, json=updated_post)     
                print('UPDATE_POST = ' + str(update))
            except:
                print('Image not found.')
