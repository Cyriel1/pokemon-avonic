from csv import reader

from ..utility.path import resource_path

from .pokemon import Pokemon


class Pokemons:
    def __init__(self):
        self.__pokemons = []
        self.__set_pokemons()

    def __set_pokemons(self):
        self.__pokemons = []
        csv_file = resource_path('app/data/pokemon.csv')

        with open(csv_file, 'r') as file:
            csvreader = reader(file)
            for row in csvreader:
                self.__pokemons.append(Pokemon(row[0], int(row[1]), int(row[2]), row[3]))

    def get_pokemons(self):
        return self.__pokemons
