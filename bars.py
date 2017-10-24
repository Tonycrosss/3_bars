import json
import sys
from math import sin, cos, sqrt, atan2


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        parsed_json_data = json.load(file_handler)
    return parsed_json_data


def get_biggest_bar(parsed_json_data):
    return max(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(parsed_json_data):
    return min(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def distance_counter(lat1, lon1, lat2, lon2):
    earth_radius = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius * c

    return distance


def get_closest_bar(parsed_json_data, longitude, latitude):
    return min(parsed_json_data['features'],
               key=lambda x: distance_counter(x['geometry']['coordinates'][0],
                                              x['geometry']['coordinates'][1],
                                              longitude,
                                              latitude))


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    print('Самый большой бар:\n')
    print(get_biggest_bar(parsed_json))
    print('\n')
    print('Самый маленький бар:\n')
    print(get_smallest_bar(parsed_json))
    print('\n')
    print('Чтобы узнать ближайший бар - укажите координаты:')
    lat2 = float(input('Введите ширину:\n'))
    lon2 = float(input('Введите долготу:\n'))
    print('Самый близкий бар:\n')
    print(get_closest_bar(parsed_json, lat2, lon2))



