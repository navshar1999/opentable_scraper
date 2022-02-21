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

