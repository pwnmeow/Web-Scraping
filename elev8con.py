import requests
from bs4 import BeautifulSoup 
baseurl ="https://www.elev8con.com/speakers/"

file = open("elev8con.txt","a", encoding="utf-8") 
page = requests.get("https://www.elev8con.com/speakers")
if(page.status_code == 200):
    print('got page ---------------------------------')
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    html = soup.findAll('h4').get_text()
    print(html)
else:
    print("no page found")
# names = []
# divs = soup.findAll(class_= 'speaker_info_wrapper')    
# for div in divs:
#     name = div.find()
#     names += name
# clear_names = ""
# for i in names:
#     clear_names += i 

# # file.write(clear_names)
# nameJoin =[]
# for name in names:
#     nameSplit= split_string(name)
#     Join = join_string(nameSplit)
#     nameJoin.append(Join)


# for name in nameJoin:
#     speaker = baseurl + name
#     page = requests.get(speaker)
#     if(page.status_code == 200):
#         soup = BeautifulSoup(page.content, 'html.parser')
#         html = soup.findAll(class_= 'linkedin')
#         a = html[1].find_all('a', href=True)
#         href = a[0]['href']
#         print(href)