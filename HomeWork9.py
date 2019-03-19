import requests
from bs4 import BeautifulSoup

r = requests.get('https://python.org')
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.title.string)