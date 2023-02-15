from dependency_injector import containers, providers

from . import team_overview_view, choose_pokemon_view, choose_opponent_view, change_pokemon_view, \
    battle_sequence_view, main_menu_view


class Views(containers.DeclarativeContainer):
    change_pokemon = providers.Singleton(change_pokemon_view.ChangePokemonView)
    battle_sequence = providers.Singleton(battle_sequence_view.BattleSequenceView, change_pokemon)
    choose_opponent = providers.Singleton(choose_opponent_view.ChooseOpponentView)
    choose_pokemon = providers.Singleton(choose_pokemon_view.ChoosePokemonView)
    team_overview = providers.Singleton(team_overview_view.TeamOverviewView)
    main_menu = providers.Singleton(main_menu_view.MainMenuView, team_overview)
