import requests
from bs4 import BeautifulSoup
import re

def linkedin(href):
    return href and re.compile("linkedin").search(href)
    

file = open("washingtonelite.txt","a", encoding="utf-8") 
page = requests.get("https://washingtonelite.com/")
if(page.status_code == 200):
    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.findAll('a')
    something= soup.find_all(href=linkedin)
    for link in something:
        print(link['href'])


    
