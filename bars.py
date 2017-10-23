import json
import sys
from math import sin, cos, sqrt, atan2


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        parsed_json_data = json.load(f)
    return parsed_json_data


def get_biggest_bar(parsed_json_data):
    return max(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(parsed_json_data):
    return min(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def distance_counter(lat1, lon1, lat2, lon2):
    r = 6373.0  # Earth radius in km

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c

    return distance


def get_closest_bar(parsed_json_data, longitude, latitude):
    return min(parsed_json_data['features'],
               key=lambda x: distance_counter(x['geometry']['coordinates'][0],
                                              x['geometry']['coordinates'][1],
                                              longitude,
                                              latitude))


if __name__ == '__main__':
    filepath = sys.argv[1]
    temp_data = load_data(filepath)
    print('Самый большой бар:\n')
    print(get_biggest_bar(temp_data))
    print('\n')
    print('Самый маленький бар:\n')
    print(get_smallest_bar(temp_data))
    print('\n')
    print('Чтобы узнать ближайший бар - укажите координаты:')
    lat2 = float(input('Введите ширину:\n'))
    lon2 = float(input('Введите долготу:\n'))
    print('Самый близкий бар:\n')
    print(get_closest_bar(temp_data, lat2, lon2))



