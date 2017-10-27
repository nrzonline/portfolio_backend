#!/bin/bash

set -e

sed -i "s/DEBUG = True/DEBUG = False/g" ../portfolio/settings/base.py 
tar -zcvf "deploy.tar.gz" ../ -X deployignore.txt
sed -i "s/DEBUG = False/DEBUG = True/g" ../portfolio/settings/base.py 

scp deploy.tar.gz nrzonline@vps.danielterhorst.nl:~/
ssh nrzonline@vps.danielterhorst.nl \
    "rm nrzonline_bu -r" \
    "&& cp nrzonline nrzonline_bu -r" \
    "&& tar xf deploy.tar.gz --directory nrzonline" \
    "&& touch nrzonline/portfolio/uwsgi.ini" \
    "&& rm deploy.tar.gz"

