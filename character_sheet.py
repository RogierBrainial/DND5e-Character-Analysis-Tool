from os import read
from urllib.request import urlopen
from pytest import TempPathFactory
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
        
        #Listed stats
        listed_base_stats = []
        listed_bonus_stats = []
        listed_override_stats = []
        
        #Listed racial traits
        listed_racial_traits = []
        
        
        #Character description
        avatarUrl  = data['data']['avataUrl']
        name = data['data']['name']
        gender = data['data']['gender']
        faith = data['data']['faith']
        age = data['data']['age']
        hair = data['data']['hair']
        eyes = data['data']['hair']
        skin = data['data']['skin']
        height = data['data']['height']
        weight = data['data']['weight']
        
        #Base stats
        inspiration = data['data']['inspiration']
        baseHP = data['data']['baseHitPoints']
        bonusHP = data['data']['bonusHitPoints']
        removedHP = data['data']['removedHitPoints']
        tempHP = data['data']['temporaryHitPoints']
        currentXP = data['data']['currentXp']
        alignmentID = data['data']['allignmentID']
        lifestyleID = data['data']['lifestyleID']
        
        for base_stat in range(data['data']['stats']):
            for all_stats in data['data']['stats']:
                listed_base_stats.append(all_stats['id'])
                listed_base_stats.append(all_stats['value'])
        for bonus_stat in data['data']['bonusStats']:
            for all_bonus_stats in range(data['data']['bonusStats']):
                listed_bonus_stats.append(all_bonus_stats['id'])
                listed_bonus_stats.append(all_bonus_stats['value'])
        for override_stat in data['data']['overrideStats']:
            for all_override_stats in range(data['data']['overrideStats']):
                listed_bonus_stats.append(all_override_stats['id'])
                listed_bonus_stats.append(all_override_stats['value'])
            
        #Character background
        hasCustomBackgorund = data['data']['background']['hasCustomBackground']
        backgroundName = data['data']['background']['definitions']['name']
        backgroundShortDescription = data['data']['background']['definitions']['shortDescription']
        backgroundFeatureDescription = data['data']['background']['definitions']['featureDescription']
        customBackgroundName = data['data']['background']['customBackground']['name']
        customBackgroundDescription = data['data']['background']['customBackground']['description']
        
        #Character race
        isSubclassRace = data['data']['race']['isSubclassRace']
        baseRaceName = data['data']['race']['baseRaceName']
        entityRaceID = data['data']['race']['entityRaceId']
        entityRaceTypeID = data['data']['race']['entityRaceTypeId']
        raceFullName =  data['data']['race']['raceFullName']
        raceDescription =  data['data']['race']['raceDescription']
        raceMoreDetailsUrl = data['data']['race']['raceMoreDetails']
        raceIsHomebrew = data['data']['race']['raceIsHomebrew']
        
        for racialTrait in range(data['data']['racialTraits']):
            for all_racial_traits in data['data']['racialTraits']:
                listed_racial_traits.append(all_racial_traits['id'])
                listed_racial_traits.append(all_racial_traits['name'])
                listed_racial_traits.append(all_racial_traits['description'])
                listed_racial_traits.append(all_racial_traits['displayConfiguration']['RACIALTRAIT'])
                listed_racial_traits.append(all_racial_traits['displayConfiguration']['ABILITYSCORE'])
                listed_racial_traits.append(all_racial_traits['displayConfiguration']['LANGUAGE'])
                listed_racial_traits.append(all_racial_traits['displayConfiguration']['CLASSFEATURE'])
        
        #Character speeds
        
                
    
        return (str(f'{avatarUrl}\n Character description:\n Name: {name}\n Gender: {gender}\n Faith: {faith}\n Age: {age}\n Hair: {hair}\n Eyes: {eyes}\n')
                + str(f'Skin: {skin}\n Height: {height}\n weight: {weight}\n'))

        
     
   
       


get_character_data(character_id=character_id_fardri)
get_character_data(character_id=character_id_frankie)
get_character_data(character_id=character_id_rutger)

print(read_character_data(character_id_fardri))
print(read_character_data(character_id_frankie))
print(read_character_data(character_id_rutger))
