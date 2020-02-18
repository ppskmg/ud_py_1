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
    #  234.   Magnitude ~   3.1       Place ➡  Poland
    properties = data['features'][i]['properties']
    result = f'{i + 1:5.0f}.\t Magnitude ~ {properties["mag"]:5.1f} \t Place ➡  {properties["place"]}'
    i += 1
    print(result)

