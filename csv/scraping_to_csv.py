import requests, csv
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = requests.get(url)
html = response.text
parsed_html = BeautifulSoup(html, 'html.parser')
quotes = parsed_html.body.select('.quote')


with open('quotes.csv', 'w', encoding='utf-8') as file:
	header_csv = ['Quote', 'Author', 'Keywords']
	writer = csv.DictWriter(file, fieldnames=header_csv, delimiter='|')
	writer.writeheader()

	for q in quotes:
		
		writer.writerow({
			'Quote':q.select('.text')[0].text, 
			'Author':q.select('.author')[0].text, 
			'Keywords':q.select('.keywords')[0].get('content')})		

with open('quotes.csv', encoding='utf-8') as file:
	reading = csv.DictReader(file, delimiter='|')
	for row in reading:
		print(f'{row["Quote"]} \n Author: {row["Author"]} \n Tags: {row["Keywords"]} \n\n')

#print(parsed_html.body.select('.quote'))
#print(tags)

#print(parsed_html.body.select('.quote'))
