from bs4 import BeautifulSoup
import urllib
import requests

header = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}

#set the url we want to visit
url = 'https://www.opentable.com/chicago-restaurant-listings'

#retrieve open_table code 
source_code = requests.get(url,headers=header)
html = source_code.content

#create BeautifulSoup object
soup = BeautifulSoup(html,features="html.parser")

#retrieve restaurant names

def get_open_restaurants():
    for entry in soup.findAll('span',{'class':'rest-row-name-text'}):
        name = entry.get_text()
        print(name)

def get_open_price_points():
    for entry in soup.findAll('i',{'class':'pricing--the-price'}):
        price = entry.get_text()
        print(price.count('$'))
    
def get_open_locations(): 
    for entry in soup.findAll('span',{'class':'rest-row-meta--location rest-row-meta-text sfx1388addContent'}):
        location = entry.get_text()
        print(location)

get_open_locations()
