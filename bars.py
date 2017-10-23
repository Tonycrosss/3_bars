import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        parsed_json_data = json.load(f)
        print("json loaded")
        # for key, value in parsed_json_data.items():
        #     for bar_params in value:
        #         print(bar_params)
    return parsed_json_data

bars_clean_list = []


def get_biggest_bar(data):
    for bar_params in data['features']:
        bars_clean_list.append(bar_params)
    return max(bars_clean_list, key=lambda x:x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(data):
    for bar_params in data['features']:
        bars_clean_list.append(bar_params)
    return min(bars_clean_list, key=lambda x:x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    pass

filepath = './bars.json'
temp_data = load_data(filepath)

print(get_biggest_bar(temp_data))
print(get_smallest_bar(temp_data))

