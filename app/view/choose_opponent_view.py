from ..utility.singleton_meta import SingletonMeta
from ..utility.terminal import clear_screen

from .base.pokemons_list_view import PokemonsListView


class ChooseOpponentView(PokemonsListView, metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self.opponent_controller = None

    def display_choose_opponent(self):
        clear_screen()
        print('Choose Opponent:\n')
        print('Select the Pokemon you want to battle by selecting the number.\n')
        self.pokemon_controller.choose_opponent_list()
        self.__enter_option()

    def __enter_option(self):
        option = input(">> ")
        self.__choose_opponent_option(option)
        if not option.isdigit() or not 1 <= int(float(option)) <= self.pokemons_amount:
            print(f'Option does not exist, please try again.'
                  f'You can choose between 1 to {self.pokemons_amount}.')
            self.__enter_option()

    def __choose_opponent_option(self, _option):
        if _option.isdigit() and 1 <= int(float(_option)) <= self.pokemons_amount:
            self.opponent_controller.choose_opponent_option(_option)

    def set_opponent_controller(self, _opponent_controller):
        self.opponent_controller = _opponent_controller
