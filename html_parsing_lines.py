# <p> </p> parsing for url

from bs4 import BeautifulSoup
import requests
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
all_lines = soup.find_all('p')

text_list = list()
for lines in all_lines:
    text = lines.get_text()
    text_list.append(text)




# <p> </p> parsing for html files

from bs4 import BeautifulSoup
import pandas as pd
from glob import glob
import os
import urllib
from os.path import abspath

def find_files(directory, pattern = '**/*.html'):
    
    return sorted(glob(os.path.join(directory, pattern), recursive=True))

urls = find_files(path) # path example : './200427_result'

path_list = list()
for i in range(len(urls)):
    path = abspath(urls[i])
    path_ = 'file:///' + path # add 'file:///' to paths
    path_list.append(path_)
    
request = urllib.request.Request(path)
opener = urllib.request.build_opener()
response = opener.open(request)
html = response.read()

soup = BeautifulSoup(html, 'html5lib')

all_lines = soup.find_all('p')

text_list = list()
for lines in all_lines:
    text = lines.get_text()
    text_list.append(text)
    
    
