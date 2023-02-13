from dependency_injector import containers, providers

from . import opponent, player, pokemons


class Models(containers.DeclarativeContainer):
    opponent = providers.Singleton(opponent.Opponent)
    player = providers.Singleton(player.Player)
    pokemons = providers.Singleton(pokemons.Pokemons)
