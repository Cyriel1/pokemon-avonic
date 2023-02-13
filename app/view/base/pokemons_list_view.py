class PokemonsListView:
    def __init__(self):
        self.pokemon_controller = None
        self.pokemons_amount = 151

    def print_pokemons_list(self, _pokemons):
        self.pokemons_amount = len(_pokemons)
        print('List of available Pokemons: \n')
        for index, pokemon in enumerate(_pokemons):
            number = index + 1
            print(f'{number}. {pokemon.get_name()}')

    def set_pokemon_controller(self, _pokemon_controller):
        self.pokemon_controller = _pokemon_controller
