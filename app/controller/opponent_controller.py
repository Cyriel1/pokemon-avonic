from dependency_injector.wiring import Provide, inject

from ..model.opponent import Opponent
from ..model.pokemons import Pokemons

from ..view.battle_sequence_view import BattleSequenceView


class OpponentController:
    @inject
    def __init__(self,
                 _opponent: Opponent = Provide[Opponent],
                 _pokemons: Pokemons = Provide[Pokemons],
                 _battle_sequence_view: BattleSequenceView = Provide[BattleSequenceView]):
        self.opponent = _opponent
        self.pokemons = _pokemons
        self.battle_sequence_view = _battle_sequence_view

    def choose_opponent_option(self, _option):
        pokemons = self.pokemons.get_pokemons()
        for index, pokemon in enumerate(pokemons):
            number = index + 1
            if int(_option).__eq__(number):
                self.opponent.set_pokemon(pokemon)
                self.battle_sequence_view.display_battle_sequence()
                self.battle_sequence_view.enter_option()
                return
