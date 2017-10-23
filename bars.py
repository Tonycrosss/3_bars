import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        parsed_json_data = json.load(f)
        print("json loaded")
        for key, value in parsed_json_data.items():
            for bar_params in value:
                print(bar_params)
    pass


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    pass

filepath = './bars.json'
load_data(filepath)
