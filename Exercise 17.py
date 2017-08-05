# Web Crawler that takes news titles from 'New York Times'

# https://www.nytimes.com/

import requests
from bs4 import BeautifulSoup

def crawler():
    url = 'https://www.nytimes.com/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('h2', {"class":"story-heading"}):
        href = link.get('a')
        print(href)

crawler()