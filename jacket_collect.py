import grequests
import requests
import random
import time
from song_collector import*
from bs4 import BeautifulSoup as bs

img_file = []
img_jacket = []
remove_list = []



def jacket():
    index_num = 0

    reqs = (grequests.get(song) for song in remy_links)
    resp = grequests.map(reqs)
    for response in resp:
        soup2 = bs(response.content, 'lxml')
        try:
            fileclass = soup2.find('div', class_= 'thumbinner')
            filelink = fileclass.find('a', href = True)
            wrem = remy_url + filelink['href']
            img_file.append(wrem)
            print(wrem)
            index_num += 1
        except AttributeError:
            remove_list.append(index_num)
            index_num += 1
            pass
    for index in remove_list:
        del remy_links[index]
        del titles[index]

def image():

    reqs = (grequests.get(img) for img in img_file)
    resp = grequests.map(reqs)

    for response in resp:
        soup3 = bs(response.content, 'lxml')
        try:
            fileclass = soup3.find('div', class_= 'fullImageLink')
            filelink = fileclass.find('a', href = True)
            wrem = remy_url + filelink['href']
            img_jacket.append(wrem)
            print(wrem)
        except AttributeError:
            pass

linklist()
song_title()
jacket()

image()
