FROM ubuntu:16.04

MAINTAINER Diego Santos

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir logs

RUN python3 -m nltk.downloader wordnet pros_cons reuters stopwords rslp punkt

ENTRYPOINT ["/docker-entrypoint.sh"]
