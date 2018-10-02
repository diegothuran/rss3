#!/usr/bin/env bash
until 1; do
    python Rss_midia.py;
    python soup_agenciabrasil.py;
    python soup_diplomatique.py;
    python soup_jornaldocomercio.py;
    #python soup_operamundi.py
    sleep 1;
done