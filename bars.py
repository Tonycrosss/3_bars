import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        parsed_json_data = json.load(f)
        print("json loaded")
        # for key, value in parsed_json_data.items():
        #     for bar_params in value:
        #         print(bar_params)
    return parsed_json_data


def get_biggest_bar(parsed_json_data):
    return max(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(parsed_json_data):
    return min(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(parsed_json_data, longitude, latitude):
    return min(parsed_json_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])


if __name__ == '__main__':
    filepath = './bars.json'
    temp_data = load_data(filepath)

    print(get_biggest_bar(temp_data))
    print(get_smallest_bar(temp_data))



