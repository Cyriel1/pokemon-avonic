from dependency_injector.wiring import Provide, inject

from ..model.pokemons import Pokemons

from ..view.choose_opponent_view import ChooseOpponentView
from ..view.choose_pokemon_view import ChoosePokemonView


class PokemonController:
    @inject
    def __init__(self,
                 _pokemons: Pokemons = Provide[Pokemons],
                 _choose_pokemon_view: ChoosePokemonView = Provide[ChoosePokemonView],
                 _choose_opponent_view: ChooseOpponentView = Provide[ChooseOpponentView]):
        self.pokemons = _pokemons
        self.choose_pokemon_view = _choose_pokemon_view
        self.choose_opponent_view = _choose_opponent_view

    def choose_pokemon_list(self):
        pokemons = self.pokemons.get_pokemons()
        self.choose_pokemon_view.print_pokemons_list(pokemons)

    def choose_opponent_list(self):
        pokemons = self.pokemons.get_pokemons()
        self.choose_opponent_view.print_pokemons_list(pokemons)
