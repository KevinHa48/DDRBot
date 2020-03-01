import requests
import random
from bs4 import BeautifulSoup as bs


#Making the soup
url = 'https://remywiki.com/DanceDanceRevolution_A_Full_Song_List'
remy_url = 'https://remywiki.com'
web_source = requests.get(url).content
soup = bs(web_source, 'lxml')


#Locating the end link of A20's song list
storage = soup.find('div', class_= 'mw-parser-output')

remy_links = []
titles = []



#Note the link list provides the romanized versions of titles with katakana/hiragana
def linklist():

    links = []
    

    for item in storage.find_all('ul')[12:]:
        for l_item in item.find_all('li'):
            end_link = l_item.find('a', href = True)
            links.append(end_link['href'])
    
    for url in links:
        full_link = remy_url + url
        remy_links.append(full_link)
    print(remy_links)


#Use this and link hrefs to it because of annoying romanization that remywiki did
def song_title():

    for item in storage.find_all('ul')[12:]:
        for l_item in item.find_all('li'):
            name = l_item.find('a').get_text()
            titles.append(name)
#linklist()
#song_title()
#print(len(titles))


#This is to access the url's for jacket covers of each song



    #for item in storage.find_all('ul')[13:]:
    #    for thumb in item.find('div', class_='thumbinner'):
    #        url = thumb.find('a', href = True)
    #        image_url = f'https://remywiki.com/{url["href"]}'
    #        remyfile.append(image_url)
    #print(remyfile)
    
    #print(remyfile)
    #problem with some songs coming up as none because some jackets are JPGS INSTEAD OF PNGS. WHY???
#linklist()
    
    
    
""" for link in remyfile:
        web_source2 = requests.get(link).content
        soup2 = bs(web_source2, 'lxml')
        #finding the actual image file
        image = soup2.find('div', class_= 'thumbinner')
    print(image)  """



            


#song_title()



        
    




""" for l_item in item.find_all('li'):
print(l_item) """
        
        
        
        
        
        
"""         contents = l_item.find('i')
        first = contents.find_all('a')[0]
        #Get the href link
        link = first.text
        #Get the name of the song
        name = first.find('title')
print(contents)
print(link)
print(first)
print(name) """









#Test
""" #Setting up the soup
url = 'http://ddrcommunity.com/ddr-difficulty-tier-list-single-play-level-14/'
web_source = requests.get(url).content
soup = bs(web_source, 'lxml')

#Locating the area of images

def cyclejackets():

    song_list = []

    for jacket in soup.find_all('dt', class_= 'gallery-icon landscape'):

        link = jacket.find('img')['src']
        song_list.append(link)
    
    ran_song = random.choice(song_list)

    return ran_song
   
  
  
  

""" 
"""
    ran = random.choice(song_list)
    ran_song = f'"{ran}"'

    return ran_song """

