FROM continuumio/miniconda3
RUN conda create -n env python=3.6
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN apt update
RUN apt install git
RUN git clone https://github.com/diegothuran/rss3
RUN cd rss3
RUN pip install -r rss3/requirements.txt
RUN conda install -c anaconda mysql-connector-python
RUN cd src/postagem/job.sh