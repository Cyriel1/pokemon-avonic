from ..utility.singleton_meta import SingletonMeta
from ..utility.terminal import clear_screen

from .base.pokemons_list_view import PokemonsListView


class ChoosePokemonView(PokemonsListView, metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self.team_overview_view = None
        self.player_controller = None

    def display_choose_pokemon(self):
        clear_screen()
        print('Choose Pokemon:\n')
        print('Select the Pokemon you want on your team by selecting the number.\n')
        self.pokemon_controller.choose_pokemon_list()
        self.player_controller.current_pokemon()
        self.__enter_option()

    def print_pokemons_list(self, _pokemons):
        super().print_pokemons_list(_pokemons)
        empty_option = self.pokemons_amount + 1
        print(f'{empty_option}. <Empty>')

    @staticmethod
    def print_current_pokemon(_active_pokemon):
        if _active_pokemon is not None:
            print(f'\nCurrent Pokemon: {_active_pokemon.get_name()}')
            return
        print('\nCurrent Pokemon: <Empty>')

    def __enter_option(self):
        option = input(">> ")
        empty_option = self.pokemons_amount + 1
        self.__choose_pokemon_option(option, empty_option)
        self.__back_option(option, empty_option)
        if not option.isdigit() or not 1 <= int(float(option)) <= empty_option:
            print(f'Option does not exist, please try again. '
                  f'You can choose between 1 to {empty_option}.')
            self.__enter_option()

    def __choose_pokemon_option(self, _option, _empty_option):
        if _option.isdigit() and 1 <= int(float(_option)) <= _empty_option:
            self.player_controller.choose_pokemon_option(_option)

    def __back_option(self, _option, _go_back_number):
        if _option.isdigit() and int(float(_option)).__eq__(_go_back_number):
            self.player_controller.go_back_option()

    def set_player_controller(self, _player_controller):
        self.player_controller = _player_controller

    # Setter instead of DI to avoid circular imports
    def set_team_overview_view(self, _team_overview_view):
        self.team_overview_view = _team_overview_view
