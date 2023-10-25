# -*- coding: utf-8 -*-

import urllib.request

pokemon_start = 252
pokemon_end = 386

for id in range(pokemon_start, pokemon_end+1):
    url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
    
    urllib.request.urlretrieve(url, f'images/{id}.png')
    