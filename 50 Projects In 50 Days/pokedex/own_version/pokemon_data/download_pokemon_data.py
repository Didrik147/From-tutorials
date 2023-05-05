# -*- coding: utf-8 -*-

import json
import requests

pokemon_start = 252
pokemon_end = 386

for id in range(pokemon_start, pokemon_end+1):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    
    pokemon = requests.get(url)
    data = pokemon.json()
    
    with open(f'data/{id}.json', 'w') as file:
        json.dump(data, file)