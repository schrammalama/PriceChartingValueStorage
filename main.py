import requests
from bs4 import BeautifulSoup
import os
import json
import datetime

URL = "https://www.pricecharting.com/offers?seller=dbmg7nns5d7fdwajruu3no6lky&status=collection"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("td", class_="number js-value js-price")

result_json_content = {}
result_json_content['timestamp'] = datetime.datetime.now().strftime('%c')
result_json_content['value'] = results.text

data_json_filename = 'result.json'

jsonDump = json.dump(result_json_content, indent=4)
with open(data_json_filename, 'a') as data_json_file:
  json.dump(jsonDump, data_json_file)
