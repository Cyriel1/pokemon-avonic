from app.containers import Application


def main():
    app = Application()
    views = app.views()
    controllers = app.controllers()
    set_controllers(views, controllers)
    main_menu = views.main_menu()
    main_menu.display_main_menu()


def set_controllers(views, controllers):
    main_menu = views.main_menu()
    team_overview = views.team_overview()
    choose_pokemon = views.choose_pokemon()
    choose_opponent = views.choose_opponent()
    change_pokemon = views.change_pokemon()
    battle_sequence = views.battle_sequence()
    main_menu.set_player_controller(controllers.player())
    team_overview.set_player_controller(controllers.player())
    choose_pokemon.set_player_controller(controllers.player())
    change_pokemon.set_player_controller(controllers.player())
    choose_opponent.set_opponent_controller(controllers.opponent())
    choose_pokemon.set_pokemon_controller(controllers.pokemon())
    choose_opponent.set_pokemon_controller(controllers.pokemon())
    battle_sequence.set_battle_controller(controllers.battle())


if __name__ == '__main__':
    main()
