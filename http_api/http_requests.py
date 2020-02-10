import requests

params = {
    'format': 'geojson',
    'starttime': '2018-01-01',
    'endtime': '2019-02-02',
    'longitude': '37.3199191',
    'latitude': '44.8857008',
    'maxradiuskm': '300',
}

url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?'

response = requests.get(url, headers={'Accept': 'application/json'}, params=params)

print(f'Request to {url}. \nStatus code {response.status_code}')

data = response.json()

i = 0
while i < len(data['features']):

    if 2.0 < int(data['features'][i]['properties']['mag']):
        print(data['features'][i]['properties']['place'])
        print(data['features'][i]['properties']['mag'])
    i += 1

# print(data)
print(data['features'][1]['properties']['mag'])

# print(data['features'][0])
