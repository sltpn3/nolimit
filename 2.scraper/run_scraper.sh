#!/bin/bash

scraper_path="."
python_path="/home/aditya/virtualenv/nolimit/bin/python"
query=$1
proxy=$2
cd $scraper_path
scraper_command='$python_path wikipedia_scrape.py -q "$query"'

if [ -n "$proxy" ]
then
	scraper_command+=' --proxy "$proxy"' 
fi
eval $scraper_command