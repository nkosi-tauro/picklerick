import os
import requests

def get_characters():
    url = 'https://rickandmortyapi.com/api/character'
    res = requests.get(url)
    characters = res.json()
    character_list = []
    for i in range(len(characters['results'])):
        character_list.append(characters['results'][i])
    return character_list
# For testing
#     print(character_list)

# get_characters()