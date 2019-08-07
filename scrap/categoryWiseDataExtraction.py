#!/usr/bin/python3
import urllib.request
from googlesearch import search

def extractContent(wiki):
    try:
        # wiki = "https://www.indiatoday.in/india/story/how-pakistani-media-reacted-to-modi-govt-s-decision-to-strip-kashmir-of-special-status-1577684-2019-08-06"
        page = urllib.request.urlopen(wiki)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page)
        title =soup.title.string

        text = ''
        textList = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
        for each in textList:
            text += each

        file1 = open('dataSet/' + title + ".txt", "w")
        file1.write(text)
        file1.close()
    except:
        pass
    # to change file access modes


def extractUrl(query):


    urlList =[]
    for j in search(query, tld="co.in", num=50, stop=1, pause=2):
        urlList.append(j)
    return urlList

categories =['Isaac Newton','Albert Einstein','Amitabh Bachchan','Donald Trump','Narendra Modi','Michael Jackson','gcp','azure','aws','cloud computing']


for each in categories:
    urlList =extractUrl(each)
    for eachUrl in urlList:
        extractContent(eachUrl)






