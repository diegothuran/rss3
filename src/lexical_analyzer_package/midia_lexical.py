#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from lexical_analyzer_package import base_lexical_analyzer


# import pandas as pd
# import string 
# import numpy as np

# stemmer = nltk.stem.RSLPStemmer()
# stemmer.stem('copiar')

# categories related to the main theme: security in this case
# SEARCH_WORDS = ['termo1',
#                 'termo1 AND termo2',
#                 'termo1 OR termo2',
#                 'termo1 OR termo2 AND termo3',
#                 'termo1 AND termo2 OR termo3',
#                 'termo1 OR termo2 OR termo3 OR termo4 OR termo5 OR termo6 OR termo7',
#                 'termo1 AND termo2 AND termo3 AND termo4 AND termo5 AND termo6 AND termo7',
#                 'termo1 OR termo2 OR termo3 AND termo4 OR termo5 AND termo6 OR termo7']

# SEARCH_WORDS = ['termo1 OR termo2 OR termo3 OR termo4 OR termo5 OR termo6 OR termo7']

WORDS = ['grupo globo',
        'organizações globo',
        'rede globo',
        'da globo',
        'globo AND governo federal OR golpe OR golpista',
        'globo AND acionista OR acionistas OR diretor OR diretores OR executivo OR executivos AND da globo OR do globo',
        'globo AND tcu OR pedaladas fiscais',
        'globo AND zelotes OR carf OR sgr',
        'globo AND nardes',
        'afiliada da globo OR afiliadas da globo',
        'afiliada da rede globo OR afiliadas da rede globo',
        'afiliada da tv globo OR afiliadas da tv globo',
        'globo AND receita AND sonegação',
        'globo AND paraty OR parati OR mossack OR triplex',
        'globo AND corrupção AND futebol',
        'globo AND hawilla OR josé maria marin OR marco polo del nero OR ricardo teixeira',
        'globo AND cbf OR fifa OR traffic',
        'globo AND ditadura OR golpe de 64 OR regime militar',
        'roberto irineu marinho',
        'joão roberto marinho',
        'josé roberto marinho',
        'irineu marinho',
        'marcelo bechara',
        'paulo tonet OR paulo tonet camargo',
        'jorge nobrega OR jorge nóbrega',
#         'paulo marinho daudt OR paulo marinho AND globo OR gloob OR viu OR globosat',
        'paulo marinho daudt OR paulo marinho AND globo OR gloob OR Viu OR globosat',
        'fundação roberto marinho',
        'família marinho OR irmãos marinho',
        'marcelo campos pinto',
        'pedro garcia AND globo'
        ]

THEME_CATEGORIES = []

def split_and_string(words):
    # Index of the first occurrence of 'AND' in words
    and_idx = words.index('AND')
    #The first index of the 'AND' word and the previous blank space
    substring_init = words[:(and_idx - 1)]
    #The first index of the 'AND' word and the posterior blank space
    substring_end = words[(and_idx + 4):]
    return substring_init, substring_end

def split_or_string(words):
    # Index of the first occurrence of 'OR' in words
    and_idx = words.index('OR')
    #The first index of the 'OR' word and the previous blank space
    substring_init = words[:(and_idx - 1)]
    #The first index of the 'OR' word and the posterior blank space
    substring_end = words[(and_idx + 3):]
    return substring_init, substring_end


def teste_and(words):
    verify_and_connector, verify_or_connector = True, True
    terms_and = []
    while(verify_and_connector):
        substring_init, words = split_and_string(words)
        # Check if there is 'OR' connector in substring_init
        terms_or = []
        if('OR' in substring_init):
            while(verify_or_connector):
                first_substring, substring_init = split_or_string(substring_init)
                terms_or.append(first_substring)
                if('OR' not in substring_init):
                    terms_or.append(substring_init)
                    verify_or_connector = False
        else:
            terms_or.append(substring_init)
        terms_and.append(terms_or)
        verify_or_connector = True
        
        if('AND' not in words):
            # Check if there is 'OR' connector in words
            terms_or = []
            if('OR' in words):
                while(verify_or_connector):
                    first_substring, words = split_or_string(words)
                    terms_or.append(first_substring)
                    if('OR' not in words):
                        terms_or.append(words)
                        verify_or_connector = False
            # Appending the last term to the list
            else:
                terms_or.append(words)
            terms_and.append(terms_or)
            verify_and_connector = False
    return terms_and
    
def teste_or(words):
    # Check if there is 'OR' connector in substring_init
    verify_or_connector = True
    terms_or = []
    while(verify_or_connector):
        first_substring, words = split_or_string(words)
        terms_or.append(first_substring)
        if('OR' not in words):
            terms_or.append(words)
            verify_or_connector = False

    return terms_or

def structure_words():
    structured_words = []
    for i in range(len(WORDS)):
        words = WORDS[i]
     
        if('AND' in words):
            terms_and = teste_and(words)
            structured_words.append(terms_and)
                 
        elif(('AND' not in words) and ('OR' in words)):
            terms_or = teste_or(words)
            structured_words.append(terms_or)
        
        else:
            structured_words.append([words])
    return structured_words
        

# if __name__ == '__main__':
#     for i in range(len(WORDS)):
#         THEME_CATEGORIES.append('categoria' + str(i))
#     clustered_words = cluster_words()
#     
# #     for i in range(len(SEARCH_WORDS)):
# #         print('\n' + str(SEARCH_WORDS[i]))
# #         print(str(THEME_CATEGORIES[i]) + ' - ' + str(clustered_words[i]))
#     
#     temp = 'O Grupo Globo falou esta manha atraves do diretor da globo de pernambuco.'
#     cats = base_lexical_analyzer.get_categories_tree_structure(temp, clustered_words, THEME_CATEGORIES)
#     print('FIM')
#     print(cats)
        

def lexical(df):
    for i in range(len(WORDS)):
        THEME_CATEGORIES.append('categoria' + str(i))
    words_tree_structure = structure_words()
    
    df, categories = base_lexical_analyzer.get_categories_corpus_tree_structure(df, words_tree_structure, THEME_CATEGORIES)
    return df, categories
  
def lexical_corpus_and_title(df):
    for i in range(len(WORDS)):
        THEME_CATEGORIES.append('categoria' + str(i))
    words_tree_structure = structure_words()
    
    df, categories = base_lexical_analyzer.get_categories_corpus_and_title_tree_structure(df, words_tree_structure, THEME_CATEGORIES)
    if(categories == [set()]):
        print(' -- no categories -- ')
    return df, categories
