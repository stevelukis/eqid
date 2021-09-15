"""
Latest Earthquake Detection Package
"""


def data_extranction():
    data = dict()
    data['date'] = '15 September 2021'
    data['time'] = '07:49:47 WIB'
    data['magnitude'] = 5.4
    data['depth'] = 20
    data['location'] = {'lat': 1.28, 'long': 122.16}
    data['center_description'] = 'Pusat gempa berada di laut 85 km BaratLaut Boalemo'
    data['affected_description'] = \
        'Dirasakan (Skala MMI): III Boalemo, II - III Buol, II Manado, II Bone Bolango, II Gorontalo, II Toli-toli'

    return data


def console_print(result):
    print('Latest Earthquake in Indonesia')
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Location: Latitude={result['location']['lat']} longitude={result['location']['long']}")
    print(f"Center: {result['center_description']}")
    print(f"Affected: {result['affected_description']}")


if __name__ == '__main__':
    result = data_extranction()
    console_print(result)
