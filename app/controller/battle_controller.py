from dependency_injector.wiring import Provide, inject
from threading import Timer
from sys import exit

from ..model.opponent import Opponent
from ..model.player import Player

from ..view.battle_sequence_view import BattleSequenceView


class BattleController:
    @inject
    def __init__(self,
                 _player: Player = Provide[Player],
                 _opponent: Opponent = Provide[Opponent],
                 _battle_sequence_view: BattleSequenceView = Provide[BattleSequenceView]):
        self.player = _player
        self.opponent = _opponent
        self.battle_sequence_view = _battle_sequence_view

    def player_status(self):
        pokemon = self.player.get_active_pokemon()
        self.battle_sequence_view.print_player_status(pokemon)

    def opponent_status(self):
        pokemon = self.opponent.get_pokemon()
        self.battle_sequence_view.print_opponent_status(pokemon)

    def attack(self):
        player_active_pokemon = self.player.get_active_pokemon()
        team = self.player.get_team()
        opponent_pokemon = self.opponent.get_pokemon()

        remaining_health = player_active_pokemon.attack(opponent_pokemon.get_health())
        opponent_pokemon.set_health(remaining_health)
        action = self.__opponent_random_command(player_active_pokemon, opponent_pokemon)
        self.__remove_active_pokemon_from_team(player_active_pokemon, team)

        self.__win(opponent_pokemon, team)
        self.__lost(team)

        self.battle_sequence_view.display_battle_sequence()
        player_log = Timer(0.1, self.battle_sequence_view.print_battle_log, [player_active_pokemon.get_name(),
                                                                             'attack'])
        opponent_log = Timer(0.2, self.battle_sequence_view.print_battle_log, [opponent_pokemon.get_name(), action])
        enter_option = Timer(0.4, self.battle_sequence_view.enter_option)
        player_log.start(), opponent_log.start(), enter_option.start()

    def special_attack(self):
        player_active_pokemon = self.player.get_active_pokemon()
        team = self.player.get_team()
        opponent_pokemon = self.opponent.get_pokemon()

        remaining_health = player_active_pokemon.special_attack(opponent_pokemon.get_health())
        opponent_pokemon.set_health(remaining_health)
        action = self.__opponent_random_command(player_active_pokemon, opponent_pokemon)
        self.__remove_active_pokemon_from_team(player_active_pokemon, team)

        self.__win(opponent_pokemon, team)
        self.__lost(team)

        self.battle_sequence_view.display_battle_sequence()
        player_log = Timer(0.1, self.battle_sequence_view.print_battle_log, [player_active_pokemon.get_name(),
                                                                             'special attack'])
        opponent_log = Timer(0.2, self.battle_sequence_view.print_battle_log, [opponent_pokemon.get_name(), action])
        enter_option = Timer(0.4, self.battle_sequence_view.enter_option)
        player_log.start(), opponent_log.start(), enter_option.start()

    def heal(self):
        player_active_pokemon = self.player.get_active_pokemon()
        team = self.player.get_team()
        opponent_pokemon = self.opponent.get_pokemon()

        player_active_pokemon.heal()
        action = self.__opponent_random_command(player_active_pokemon, opponent_pokemon)
        self.__remove_active_pokemon_from_team(player_active_pokemon, team)

        self.__win(opponent_pokemon, team)
        self.__lost(team)

        self.battle_sequence_view.display_battle_sequence()
        player_log = Timer(0.1, self.battle_sequence_view.print_battle_log, [player_active_pokemon.get_name(), 'heal'])
        opponent_log = Timer(0.2, self.battle_sequence_view.print_battle_log, [opponent_pokemon.get_name(), action])
        enter_option = Timer(0.4, self.battle_sequence_view.enter_option)
        player_log.start(), opponent_log.start(), enter_option.start()

    def __opponent_random_command(self, _player_active_pokemon, _opponent_pokemon):
        command = self.opponent.random_command(_player_active_pokemon.get_health())
        action, remaining_health = command
        if action.__eq__('attack') or action.__eq__('special attack'):
            _player_active_pokemon.set_health(remaining_health)
        return action

    def __remove_active_pokemon_from_team(self, _player_active_pokemon, _team):
        if _player_active_pokemon.get_health().__eq__(0) and len(_team) > 1:
            self.player.remove_pokemon(_player_active_pokemon)
            self.player.set_active_pokemon(_team[0])
            defeated_log = Timer(0.3, self.battle_sequence_view.print_defeated_log, [_player_active_pokemon.get_name()])
            defeated_log.start()

    def __win(self, _opponent_pokemon, _team):
        if _opponent_pokemon.get_health().__eq__(0):
            self.battle_sequence_view.print_win_log(_opponent_pokemon.get_name())
            exit(0)

    def __lost(self, _team):
        if len(_team).__eq__(1):
            last_pokemon = self.player.get_active_pokemon()
            if last_pokemon.get_health().__eq__(0):
                self.battle_sequence_view.print_lost_log(last_pokemon.get_name())
                exit(0)
