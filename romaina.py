import requests
from bs4 import BeautifulSoup 
def split_string(string): 
  
    # Split the string based on space delimiter 
    list_string = string.split(' ') 
      
    return list_string 
  
def join_string(list_string): 
  
    # Join the string based on '-' delimiter 
    string = '-'.join(list_string) 
      
    return string
baseurl ="https://www.romaniablockchainsummit.com/speaker/"

file = open("RomaniaSpeakers.txt","a", encoding="utf-8") 
page = requests.get("https://www.romaniablockchainsummit.com")
if(page.status_code == 200):
    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find('h4').get_text()
names = []
divs = soup.findAll(class_= 'speaker_info_wrapper')    
for div in divs:
    name = div.find()
    names += name
clear_names = ""
for i in names:
    clear_names += i 

# file.write(clear_names)
nameJoin =[]
for name in names:
    nameSplit= split_string(name)
    Join = join_string(nameSplit)
    nameJoin.append(Join)


for name in nameJoin:
    speaker = baseurl + name
    page = requests.get(speaker)
    if(page.status_code == 200):
        soup = BeautifulSoup(page.content, 'html.parser')
        html = soup.findAll(class_= 'linkedin')
        a = html[1].find_all('a', href=True)
        href = a[0]['href']
        print(href)