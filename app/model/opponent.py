from copy import deepcopy
from random import shuffle


class Opponent:
    def __init__(self):
        self.__pokemon = None

    def random_command(self, _player_health):
        commands = [self.__pokemon.attack,
                    self.__pokemon.special_attack,
                    self.__pokemon.heal]
        shuffle(commands)
        match commands[0].__name__:
            case 'attack':
                return 'attack', self.__pokemon.attack(_player_health)
            case 'special_attack':
                return 'special attack', self.__pokemon.special_attack(_player_health)
            case 'heal':
                return 'heal', self.__pokemon.heal()

    def set_pokemon(self, _pokemon):
        self.__pokemon = deepcopy(_pokemon)

    def get_pokemon(self):
        return self.__pokemon
