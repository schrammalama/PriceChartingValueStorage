import requests
from bs4 import BeautifulSoup
import os
import json
import datetime

URL = "https://www.pricecharting.com/offers?seller=dbmg7nns5d7fdwajruu3no6lky&status=collection"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("td", class_="number js-value js-price")

timestamp = datetime.datetime.now().strftime('%c')
value = results.text

data_json_filename = 'result.json'

with open(data_json_filename, 'a') as data_json_file:
  json.dumps({"Time": timestamp, "Value": value}, sort_keys=True, indent=4)
  json.dump(data_json_file)
