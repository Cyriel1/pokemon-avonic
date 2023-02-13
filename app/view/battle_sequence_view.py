from dependency_injector.wiring import Provide, inject
from threading import Lock

from ..utility.singleton_meta import SingletonMeta
from ..utility.terminal import clear_screen

from .change_pokemon_view import ChangePokemonView


class BattleSequenceView(metaclass=SingletonMeta):
    @inject
    def __init__(self,
                 _change_pokemon_view: ChangePokemonView = Provide[ChangePokemonView]):
        self.battle_controller = None
        self.change_pokemon_view = _change_pokemon_view

    def display_battle_sequence(self):
        clear_screen()
        print('Battle!\n')
        self.battle_controller.opponent_status()
        self.battle_controller.player_status()
        self.__print_commands()

    def print_opponent_status(self, _pokemon):
        print('Opponent:\n')
        self.__print_status(_pokemon)

    def print_player_status(self, _pokemon):
        print('Player:\n')
        self.__print_status(_pokemon)

    @staticmethod
    def print_battle_log(_name, _action):
        with Lock():
            print(f'{_name} used {_action}!')

    @staticmethod
    def print_defeated_log(_name):
        with Lock():
            print(f'{_name} was defeated! Changing pokemon...')

    @staticmethod
    def print_win_log(_name):
        print(f'Enemy {_name} Fainted!')
        print('You won!')
        print('Player got 1500 pokédollars!')

    @staticmethod
    def print_lost_log(_name):
        print(f'{_name} Fainted!')
        print('You lost!')
        print('Player blacked out. 35000 pokédollars have been taken!')

    @staticmethod
    def __print_status(_pokemon):
        status = [f'Pokemon: {_pokemon.get_name()}',
                  f'HP: {_pokemon.get_health()}/{_pokemon.get_max_health()}',
                  f'ATK: {int(_pokemon.get_attack() / 2)}/{_pokemon.get_attack()}',
                  f'Type: {_pokemon.get_type()}']
        for state in status:
            print(state)
        print('')

    @staticmethod
    def __print_commands():
        print('Available Commands:\n')
        options = ['1. Attack', '2. Special Attack', '3. Heal', '4. Change Team']
        for option in options:
            print(option)
        print('')

    def enter_option(self):
        option = input('>> ')
        match option:
            case '1':
                self.battle_controller.attack()
            case '2':
                self.battle_controller.special_attack()
            case '3':
                self.battle_controller.heal()
            case '4':
                self.change_pokemon_view.display_change_pokemon()
            case _:
                print('Option does not exist, please try again. '
                      'You can choose between 1 to 4.')
                self.enter_option()

    def set_battle_controller(self, _battle_controller):
        self.battle_controller = _battle_controller
