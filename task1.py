import requests
from pprint import pprint


def the_smartest_hero():
    url = "https://superheroapi.com/api/2619421814940190/search/"
    names_list = ('Hulk', 'Captain America', 'Thanos')

    merged_dict = {}

    for name in names_list:
        url_for_hero_name = f'{url}{name}'
        response = requests.get(url_for_hero_name)
        data = response.json()

        full_file = data['results']
        for i in full_file:
            if i['name'] in names_list:
                required_dict_with_name_and_intelligence = {i['name']: int(i['powerstats']['intelligence'])}

        merged_dict.update(required_dict_with_name_and_intelligence)

    print(f'The smartest hero is {max(merged_dict, key=merged_dict.get)}')

    if response.status_code != 200:
        print("Запрос не успешен")
        return


if __name__ == '__main__':
    the_smartest_hero()

