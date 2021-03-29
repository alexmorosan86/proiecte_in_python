import unittest
from pokemon import Pokemon
import requests
from unittest.mock import  patch

class OurResponse(requests.Response):
  def json(self):
    return {'species':{'name':"pikachu"}}



class TestPokemon(unittest.TestCase):
  @patch('requests.get', return_value= OurResponse())
  def test_pikachu(self,get):
    pokemon = Pokemon()
    value = pokemon.get_by_number(25)
    self.assertEqual('pikachu', value)


