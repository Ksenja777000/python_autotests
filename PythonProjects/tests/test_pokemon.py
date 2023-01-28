import requests
import pytest

def  test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/pokemons')
    assert response.status_code == 200


def test_fragment_of_response():
     response = requests.get('https://pokemonbattle.me:5000/pokemons', params = {'pokemon_id': '3539'})
     assert response.json()['name'] == 'Vend'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Fuksis'), ('city', 'Moscow')])

def test_parametr(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id': '1873'}) 
    assert response.json()[key] == value
