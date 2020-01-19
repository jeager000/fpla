import requests
from termcolor import colored
import os

baner="""
  __       _
 / _|_ __ | | __ _   |  Code by: jeager
| |_| '_ \| |/ _` |  |  Youtube: CACACRACK
|  _| |_) | | (_| |  |  Instagram: jeager000
|_| | .__/|_|\__,_|  |  Github: https://github.com/jeager000
    |_| Finder Page Login Admin
"""
print(colored(baner,'green'))

link=str(input(colored('link: ','yellow')))
list_page=open('page.txt','r')
page_list=list_page.readlines()
list_page.close()

for page in page_list:
  admin=page.strip()
  adminn='/'+admin
  URL=link+adminn
  
  x=requests.get(URL)
  if x.status_code == 200:
    print(colored('Found: '+URL,'green'))
    break
  else:
    print(colored('Not found: '+URL,'red'))
    
  
  