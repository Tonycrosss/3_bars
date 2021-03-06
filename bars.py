import json
import sys
from math import sin, cos, sqrt, atan2


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        parsed_json_data = json.load(file_handler)
    return parsed_json_data


def get_biggest_bar_name(parsed_json_data):
    return max(parsed_json_data['features'],
               key=lambda x: x['properties']
               ['Attributes']
               ['SeatsCount'])['properties']['Attributes']['Name']


def get_smallest_bar_name(parsed_json_data):
    return min(parsed_json_data['features'],
               key=lambda x: x['properties']
               ['Attributes']
               ['SeatsCount'])['properties']['Attributes']['Name']


def distance_calculation(lat1, lon1, lat2, lon2):
    earth_radius = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius * c

    return distance


def get_closest_bar_name(parsed_json_data, longitude, latitude):
    closest_bar_info = min(parsed_json_data['features'],
                           key=lambda x: distance_calculation
                           (x['geometry']['coordinates'][0],
                            x['geometry']['coordinates'][1],
                            longitude,
                            latitude))
    return closest_bar_info['properties']['Attributes']['Name']


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    print('Самый большой бар:')
    print(get_biggest_bar_name(parsed_json))
    print('\n')
    print('Самый маленький бар:')
    print(get_smallest_bar_name(parsed_json))
    print('\n')
    print('Чтобы узнать ближайший бар - укажите координаты:')
    lat2 = float(input('Введите ширину:\n'))
    lon2 = float(input('Введите долготу:\n'))
    print('Самый близкий бар:')
    print(get_closest_bar_name(parsed_json, lat2, lon2))
