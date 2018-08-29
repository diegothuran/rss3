#!/usr/bin/env bash
a = 1;
until [$_done]; do
    python Rss_test.py;
    python post_from_bbc.py;
    python soup_elpais.py;
    python soup_globo.py;
    sleep 1;
done