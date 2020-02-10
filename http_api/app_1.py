import requests
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

data = response.json()
print(f'\nRequest to {url}. \nStatus code {response.status_code}\n')


i = 0
while i < len(data['features']):
    #  234.   Magnitude ~   3.1       Place ➡  Poland
    properties = data['features'][i]['properties']
    result = f'{i + 1:5.0f}.\t Magnitude ~ {properties["mag"]:5.1f} \t Place ➡  {properties["place"]}'
    i += 1
    print(result)


# TODO: try errors
# TODO: ssl
# TODO: timout
