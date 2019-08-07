#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup



def extractUrl(url):
    html = requests.get(url).text
    bs = BeautifulSoup(html)
    list_of_link=[]
    possible_links = bs.find_all('a')
    for link in possible_links:
        if link.has_attr('href'):
            tempLink = link.attrs['href']

            list_of_link.append(tempLink)


    return list_of_link



