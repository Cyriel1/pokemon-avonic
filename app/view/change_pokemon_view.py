from ..utility.singleton_meta import SingletonMeta
from ..utility.terminal import clear_screen


class ChangePokemonView(metaclass=SingletonMeta):
    def __init__(self):
        self.player_controller = None
        self.team_amount = 6

    def display_change_pokemon(self):
        clear_screen()
        print('Change Pokemon:\n')
        print('Choose the Pokemon you fight with by selecting the number.\n')
        self.player_controller.change_pokemon_list()
        self.__enter_option()

    def print_team_list(self, _team):
        self.team_amount = len(_team)
        for index, pokemon in enumerate(_team):
            number = index + 1
            print(f'{number}. {pokemon.get_name()}')

    def __enter_option(self):
        option = input(">> ")
        self.__change_pokemon_option(option)
        if not option.isdigit() or not 1 <= int(float(option)) <= self.team_amount:
            print(f'Option does not exist, please try again.')
            self.__enter_option()

    def __change_pokemon_option(self, option):
        if option.isdigit() and 1 <= int(float(option)) <= self.team_amount:
            self.player_controller.change_pokemon_option(option)

    def set_player_controller(self, _player_controller):
        self.player_controller = _player_controller
