from dependency_injector import containers, providers

from . import opponent_controller, player_controller, pokemon_controller, battle_controller
from ..model import models
from ..view import views


class Controllers(containers.DeclarativeContainer):
    models = providers.Container(models.Models)
    views = providers.Container(views.Views)

    pokemon = providers.Singleton(pokemon_controller.PokemonController,
                                  models().pokemons,
                                  views().choose_pokemon,
                                  views().choose_opponent)
    opponent = providers.Singleton(opponent_controller.OpponentController,
                                   models().opponent,
                                   models().pokemons,
                                   views().battle_sequence)
    player = providers.Singleton(player_controller.PlayerController,
                                 models().player,
                                 models().pokemons,
                                 views().team_overview,
                                 views().choose_opponent,
                                 views().choose_pokemon,
                                 views().change_pokemon,
                                 views().battle_sequence)
    battle = providers.Singleton(battle_controller.BattleController,
                                 models().player,
                                 models().opponent,
                                 views().battle_sequence)
