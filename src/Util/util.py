# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import requests


def get_sharedcount_info(tracked_url):
    URL = 'https://api.sharedcount.com/v1.0/'
    api_key = '8a2cccc01f801d984aa5995bc3d3594bed656a51'
      
    payload = {'apikey': api_key, 'url': tracked_url}
    r = requests.get(URL, params=payload)
    info = r.json()
    
    # Pinterest info
    pinterest = info['Pinterest']
    # Facebook info
    fb_comment = info['Facebook']['comment_count'] + info['Facebook']['comment_plugin_count']
    fb_share = info['Facebook']['share_count']
    fb_reaction = info['Facebook']['reaction_count']
    fb_total = info['Facebook']['total_count']
    
    return pinterest, fb_comment, fb_share, fb_reaction, fb_total

