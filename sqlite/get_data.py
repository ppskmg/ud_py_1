import requests
from bs4 import BeautifulSoup 

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="test_app_magnitude")
location = geolocator.geocode(input('Enter the city: ⇛ '))

longitude = str(location.longitude)
latitude = str(location.latitude)
starttime = input('Start year ⇛ ') + '-01-01'
endtime = input('End year ⇛ ') + '-01-01'
maxradiuskm = input('Search radius (km) ⇛ ')
minmagnitude = input('Min magnitude ⇛ ')


url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params = {
    'format': 'geojson',
    'starttime': starttime,
    'endtime': endtime,
    'longitude': longitude,
    'latitude': latitude,
    'maxradiuskm': maxradiuskm,
    'minmagnitude': minmagnitude,
})

if response.status_code != 200:
	print(f'Request to {url}. \nStatus code {response.status_code}')


data = response.json()

def get_data():
	data_set = []
	i = 0
	while i < len(data['features']):
	    properties = data['features'][i]['properties']
	    data_set.append((properties["mag"], properties["place"]))
	    i += 1
	return data_set





