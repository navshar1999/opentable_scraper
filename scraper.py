from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

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
    names = []
    for entry in soup.findAll('span',{'class':'rest-row-name-text'}):
        names.append(entry.get_text())
    return names 
        

def get_open_price_points():
    prices = []
    for entry in soup.findAll('i',{'class':'pricing--the-price'}):
        prices.append(entry.get_text().count('$'))
    return prices 
    
    
def get_open_locations(): 
    locations = []
    for entry in soup.findAll('span',{'class':'rest-row-meta--location rest-row-meta-text sfx1388addContent'}):
        locations.append(entry.get_text())
    return locations

#manipulating data

names = get_open_restaurants()
prices = get_open_price_points()
locations = get_open_locations()

data = np.array((names,prices,locations)).T
df = pd.DataFrame(data, columns=["name","price","location"])



