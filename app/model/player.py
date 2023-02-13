from copy import deepcopy

from .pokemon import Pokemon


class Player:
    def __init__(self):
        self.__team = []
        self.__team_limit = 6
        self.__active_pokemon = Pokemon(_name='Pikachu', _health=120, _attack=40, _type='ELECTRIC')
        self.__team.append(self.__active_pokemon)

    def add_pokemon(self, _pokemon):
        if len(self.__team) <= self.__team_limit:
            self.__team.append(deepcopy(_pokemon))

    def remove_pokemon(self, _pokemon):
        self.__team.remove(_pokemon)

    def clear_team(self):
        self.__team = []

    def get_team(self):
        return self.__team

    def set_active_pokemon(self, _pokemon):
        if _pokemon in self.__team:
            self.__active_pokemon = _pokemon
            return
        self.__active_pokemon = None

    def get_active_pokemon(self):
        return self.__active_pokemon
