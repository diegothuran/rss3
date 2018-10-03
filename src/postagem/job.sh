#!/usr/bin/env bash
until 1; do
    for f in *.py; do python "$f"; done
    sleep 1;
done