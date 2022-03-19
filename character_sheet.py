from os import read
from urllib.request import urlopen
import requests
import json

character_id_rutger = '52045993'
character_id_frankie = '52196526'
character_id_fardri = '53451164'


def get_character_data(character_id):
    # parameter for urlopen
    url = f"https://character-service.dndbeyond.com/character/v3/character/{character_id}"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())
    json_string = json.dumps(data_json)

    with open(f'{character_id}_json_data.json', 'w') as outfile:
        outfile.write(json_string)


def read_character_data(character_id):
    with open(f'{character_id}_json_data.json') as json_file:
        data = json.load(json_file)
        name = data['data']['name']
        backstory = data['data']['notes']['backstory']
        age = data['data']['age']
        campaign_name = data['data']['campaign']['name']
        characters_in_campaign0 = data['data']['campaign']['characters'][0]['characterName']
        characters_in_campaign1 = data['data']['campaign']['characters'][1]['characterName']
        characters_in_campaign2 = data['data']['campaign']['characters'][2]['characterName']
        DM = data['data']['campaign']['dmUsername']
        return str(f'Campaign: {campaign_name}\nDM: {DM}\nCharacters in campaign: {characters_in_campaign0}, {characters_in_campaign1}, {characters_in_campaign2}\nName: {name}\nAge: {age}\nBackstory: \n{backstory}')


get_character_data(character_id=character_id_fardri)
get_character_data(character_id=character_id_frankie)
get_character_data(character_id=character_id_rutger)

print(read_character_data(character_id_fardri))
print(read_character_data(character_id_frankie))
print(read_character_data(character_id_rutger))
