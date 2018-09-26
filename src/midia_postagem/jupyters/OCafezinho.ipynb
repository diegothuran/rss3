{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "sys.path.insert(0, '../../src')\n",
    "import feedparser\n",
    "import pandas as pd\n",
    "\n",
    "import urllib\n",
    "\n",
    "from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio\n",
    "from lexical_analyzer_package import midia_lexical\n",
    "from midia_postagem import midia_post\n",
    "from Model.News import News\n",
    "from Database import midia_table\n",
    "\n",
    "from newsplease import NewsPlease\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "link = 'https://www.ocafezinho.com/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "req = requests.get(link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "noticias = BeautifulSoup(req.text, \"html.parser\").find_all('div', class_='highlight text-center')\n",
    "noticias = BeautifulSoup(req.text, \"html.parser\").find_all('div', class_='box')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.ocafezinho.com/2018/09/25/obaoba/\n",
      "['Ibope: oba-oba cirandeiro não pode contaminar a esquerda']\n",
      "news_in_db: False\n",
      " -- no categories -- \n"
     ]
    }
   ],
   "source": [
    "for noticia in noticias:\n",
    "    print(noticia.find_all('a', href=True)[0]['href'])\n",
    "    article = NewsPlease.from_url(noticia.find_all('a', href=True)[0]['href'])\n",
    "    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}\n",
    "    if (article is not None):\n",
    "        row['titulos'].append(article.title)\n",
    "        row['noticia'].append(article.text)\n",
    "        row['links'].append(article.url)\n",
    "        row['abstract'].append(article.text)\n",
    "        row['date'].append(article.date_publish)\n",
    "        path_image = article.image_url\n",
    "        if path_image == '' or path_image == None:\n",
    "            row['image'].append(0)\n",
    "        else:\n",
    "            row['image'].append(download_and_move_image(article.image_url))\n",
    "        news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])\n",
    "        try:\n",
    "            print(row['titulos'])\n",
    "            news_in_db = midia_table.check_news(news)\n",
    "            print('news_in_db: ' + str(news_in_db))\n",
    "            if (not news_in_db):\n",
    "                row = pd.DataFrame(row)\n",
    "                df, categories = midia_lexical.lexical_corpus_and_title(row)\n",
    "                # DB categories\n",
    "                if (categories != [set()]):\n",
    "                    news.set_categories(categories)\n",
    "                    midia_table.save_news(news)\n",
    "                    midia_post.post_news(df)\n",
    "        except:\n",
    "            print('Empty News')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"highlight text-center\">\n",
       "<h1><a href=\"https://www.ocafezinho.com/2018/09/25/obaoba/\">Ibope: oba-oba cirandeiro não pode contaminar a esquerda</a></h1>\n",
       "<a href=\"https://www.ocafezinho.com/2018/09/25/obaoba/\">\n",
       "<img alt=\"\" class=\"img-responsive center-block wp-post-image\" height=\"462\" sizes=\"(max-width: 823px) 100vw, 823px\" src=\"https://www.ocafezinho.com/wp-content/uploads/2018/09/bolsonaro1-compressed.jpg\" srcset=\"https://www.ocafezinho.com/wp-content/uploads/2018/09/bolsonaro1-compressed.jpg 823w, https://www.ocafezinho.com/wp-content/uploads/2018/09/bolsonaro1-compressed-400x225.jpg 400w, https://www.ocafezinho.com/wp-content/uploads/2018/09/bolsonaro1-compressed-768x431.jpg 768w\" width=\"823\"> </img></a>\n",
       "</div>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "noticias[0]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
