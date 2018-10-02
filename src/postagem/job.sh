#!/usr/bin/env bash
until 1; do
    python Rss_test.py;
    python post_from_bbc.py;
    python soup_elpais.py;
    python soup_gauchazh.py
    python soup_globo.py;
    sleep 1;
done