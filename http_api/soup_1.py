import requests
from bs4 import BeautifulSoup


url = 'https://sites.google.com/site/duovpage/spargalka-po-vim'
response = requests.get(url)

html = response.text

parsed_html = BeautifulSoup(html, 'html.parser')
td = parsed_html.select('td')
# print(td[3].get_text())

for i in td:
    print(i)