# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

hit_list = [ 
    'https://www.jornalopcao.com.br/feed/'
    ]

future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]

entries = []
for feed in future_calls:
    entries.extend(feed["items"])


for entrie in entries:
    ref_link = entrie['link']
    print(ref_link)



