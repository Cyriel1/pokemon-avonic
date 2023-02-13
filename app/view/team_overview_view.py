from dependency_injector.wiring import Provide, inject

from ..utility.singleton_meta import SingletonMeta
from ..utility.terminal import clear_screen

from .choose_pokemon_view import ChoosePokemonView


class TeamOverviewView(metaclass=SingletonMeta):
    @inject
    def __init__(self,
                 _choose_pokemon_view: ChoosePokemonView = Provide[ChoosePokemonView]):
        self.choose_pokemon_view = _choose_pokemon_view
        self.main_menu_view = None
        self.player_controller = None
        self.choose_pokemon_view.set_team_overview_view(self)

    def display_team_overview(self):
        clear_screen()
        print('Team Overview:\n')
        print('Add or edit a pokemon by selecting the number.\n')
        self.player_controller.team_overview_list()
        self.print_back_option()
        self.__enter_option()

    @staticmethod
    def print_team_list(_team):
        for index in range(0, 6):
            number = index + 1
            if not _team or number > len(_team):
                print(f'{number}. <Empty>')
                continue
            print(f'{number}. {_team[index].get_name()}')

    @staticmethod
    def print_back_option():
        print('\n7. Go Back')

    def __enter_option(self):
        option = input(">> ")
        self.__edit_pokemon_option(option)
        self.__back_option(option)
        if not option.isdigit() or not 1 <= int(float(option)) <= 7:
            print('Option does not exist, please try again. '
                  'You can choose between 1 to 7.')
            self.__enter_option()

    def __edit_pokemon_option(self, option):
        if option.isdigit() and 1 <= int(float(option)) <= 6:
            self.player_controller.edit_team_option(option)

    def __back_option(self, option):
        if option.isdigit() and int(float(option)).__eq__(7):
            self.main_menu_view.display_main_menu()

    def set_player_controller(self, _player_controller):
        self.player_controller = _player_controller

    # Setter instead of DI to avoid circular imports
    def set_main_menu_view(self, _main_menu_view):
        self.main_menu_view = _main_menu_view
