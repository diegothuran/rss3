#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import base64
import datetime
import numpy as np

from Util import util

USER = b'admxarx'
PASSWORD = b'!xarx@2018*'

# URL = 'https://seguranca.xarx.rocks/wp-json/wp/v2'
URL = 'https://varejo.xarx.rocks/wp-json/wp/v2'

token = base64.standard_b64encode(USER + b':' + PASSWORD)
headers = {b'Authorization': b'Basic ' + token}

# categoria sem_categoria : 1
INDEX_CATEGORIES = {'ac' : 28,
                    'al' : 18,
                    'ap' : 29,
                    'am' : 30,
                    'ba' : 19,
                    'ce' : 20,
                    'df' : 13,
                    'es' : 36,
                    'go' : 14,
                    'ma' : 21,
                    'mt' : 15,
                    'ms' : 16,
                    'mg' : 37,
                    'pa' : 31,
                    'pb' : 22,
                    'pr' : 41,
                    'pe' : 23,
                    'pi' : 24,
                    'rj' : 38,
                    'rn' : 25,
                    'rs' : 42,
                    'ro' : 32,
                    'rr' : 33,
                    'sc' : 43,
                    'sp' : 39,
                    'se' : 26,
                    'to' : 34,
    
                    'jungmann' : 8, 
                    'haddad' : 10, 
                    'bolsonaro' : 9
                    }


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
        categories = util.get_categories_idx(categories_names, INDEX_CATEGORIES)
        cats = util.join_strings(np.array(categories).astype(str).tolist())
        
        # the text of the 'abstract' and the link
        # texto_sumarizado: por enquanto apenas em seguranca
        news = row['abstract']
        reduced_news = util.get_reduced_news(news)
        temp = '... <p>Leia a íntegra em: ' + '<a href=' + row['links'] +'> ' + row['links']  + '</a>'
        
        content = reduced_news + temp

        # if the row does not have category
        if(categories == []):
            cats = '1' # category sem categoria
           
        # url
        url = URL

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
                image_path = row['image']
                media = {'file': open(image_path,'rb'), 'caption': 'picture'}
                image = requests.post(url + '/media', headers=headers, files=media)  
                print('IMAGE_POST = ' + str(image))      
                   
                img_id = (json.loads(image.content))['id']
                post_id = (json.loads(r.content))['id']
                print(img_id)
                print(post_id)
                              
                updated_post = {'featured_media' : img_id}
                               
                update = requests.post(url + '/posts/' + str(post_id), headers=headers, json=updated_post)     
                print('UPDATE_POST = ' + str(update))
            except:
                print('Image not found.')
