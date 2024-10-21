# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

#TODO - break up into functions

 
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.meetup.com/the-london-warhammer-gaming-guild/events/'
response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.content,'lxml')
print(f'soup is of type {type(soup)}')

# Extract the __NEXT_DATA__ script tag content
next_data_script = soup.find('script', id="__NEXT_DATA__")

# Load the content as JSON
next_data = json.loads(next_data_script.string)
print(f'next data is of type {type(next_data)}')

with open("next_data.json", "w") as file:
    file.write(str(next_data))

# stick it in a pandas DataFrame
# df = pd.json_normalize(next_data)

#TODO - get the event data from next_data variable (json)