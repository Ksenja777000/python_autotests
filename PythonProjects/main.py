import requests
import json

token = 'ef4d7307e800be27f332e077d341968f'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token': token},
json = {
    "name": "Fuksis",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
 
pokemon_id = response.json()['id'] 



print(response.text) 


response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token': 
token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Vend",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
    
print(response_change.text)    


response_catch = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 'trainer_token': token},
json = {
    "pokemon_id": pokemon_id,
})

print(response_catch.text)







