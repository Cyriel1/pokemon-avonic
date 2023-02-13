from dependency_injector.wiring import Provide, inject

from ..model.player import Player
from ..model.pokemons import Pokemons

from ..view.team_overview_view import TeamOverviewView
from ..view.choose_opponent_view import ChooseOpponentView
from ..view.choose_pokemon_view import ChoosePokemonView
from ..view.change_pokemon_view import ChangePokemonView
from ..view.battle_sequence_view import BattleSequenceView


class PlayerController:
    @inject
    def __init__(self,
                 _player: Player = Provide[Player],
                 _pokemons: Pokemons = Provide[Pokemons],
                 _team_overview_view: TeamOverviewView = Provide[TeamOverviewView],
                 _choose_opponent_view: ChooseOpponentView = Provide[ChooseOpponentView],
                 _choose_pokemon_view: ChoosePokemonView = Provide[ChoosePokemonView],
                 _change_pokemon_view: ChangePokemonView = Provide[ChangePokemonView],
                 _battle_sequence_view: BattleSequenceView = Provide[BattleSequenceView]):
        self.player = _player
        self.pokemons = _pokemons
        self.team_overview_view = _team_overview_view
        self.choose_opponent_view = _choose_opponent_view
        self.choose_pokemon_view = _choose_pokemon_view
        self.change_pokemon_view = _change_pokemon_view
        self.battle_sequence_view = _battle_sequence_view

    def does_team_exist(self):
        team = self.player.get_team()
        if team:
            self.choose_opponent_view.display_choose_opponent()
            return True
        return False

    def team_overview_list(self):
        team = self.player.get_team()
        self.team_overview_view.print_team_list(team)

    def choose_pokemon_option(self, _option):
        pokemons = self.pokemons.get_pokemons()
        active_pokemon = self.player.get_active_pokemon()
        self.__remove_active_pokemon_if_exist(active_pokemon)
        for index, pokemon in enumerate(pokemons):
            number = index + 1
            if int(_option).__eq__(number):
                self.player.add_pokemon(pokemon)
                self.__set_active_pokemon_to_first_member()
                self.team_overview_view.display_team_overview()
                return

    def go_back_option(self):
        self.__set_active_pokemon_to_first_member()
        self.team_overview_view.display_team_overview()

    def change_pokemon_list(self):
        team = self.player.get_team()
        self.change_pokemon_view.print_team_list(team)

    def edit_team_option(self, _option):
        if not self.__set_selected_pokemon(_option):
            self.player.set_active_pokemon(None)
        self.choose_pokemon_view.display_choose_pokemon()

    def current_pokemon(self):
        active_pokemon = self.player.get_active_pokemon()
        self.choose_pokemon_view.print_current_pokemon(active_pokemon)

    def change_pokemon_option(self, _option):
        self.__set_selected_pokemon(_option)
        self.battle_sequence_view.display_battle_sequence()
        self.battle_sequence_view.enter_option()

    def __set_active_pokemon_to_first_member(self):
        team = self.player.get_team()
        if team:
            self.player.set_active_pokemon(team[0])

    def __set_selected_pokemon(self, _option):
        team = self.player.get_team()
        for index, pokemon in enumerate(team):
            number = index + 1
            if int(_option).__eq__(number):
                self.player.set_active_pokemon(pokemon)
                return True
        return False

    def __remove_active_pokemon_if_exist(self, _active_pokemon):
        if _active_pokemon is not None:
            self.player.remove_pokemon(_active_pokemon)
            self.player.set_active_pokemon(None)
