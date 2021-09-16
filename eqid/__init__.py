import requests
from bs4 import BeautifulSoup

_url = 'https://www.bmkg.go.id/'


def _extract_data():
    response = requests.get(_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('span', attrs={'class': 'waktu'})
    result = result.text.split(', ')
    date = result[0]
    time = result[1]

    result = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
    result = result.findChildren('li')

    magnitude = result[1].text
    depth = result[2].text

    location_raw = result[3].text
    location_raw = location_raw.split(' LS - ')
    lat = location_raw[0]
    long = location_raw[1].replace(' BT', '')

    center_desc = result[4].text
    affected_desc = result[5].text

    data = dict()
    data['date'] = date
    data['time'] = time
    data['magnitude'] = magnitude
    data['depth'] = 20
    data['location'] = {'lat': lat, 'long': long}
    data['center_desc'] = center_desc
    data['affected_desc'] = affected_desc

    return data


def get_data():
    return _extract_data()


def console_print(result):
    print('Latest Earthquake in Indonesia')
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Location: Latitude={result['location']['lat']} longitude={result['location']['long']}")
    print(f"Center: {result['center_desc']}")
    print(f"Affected: {result['affected_desc']}")
