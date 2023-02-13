from random import randint


class Pokemon:
    def __init__(self, _name, _health, _attack, _type):
        self.__name = _name
        self.__health = _health
        self.__max_health = _health
        self.__attack = _attack
        self.__type = _type

    def attack(self, _enemy_health):
        attack_value = randint(int(self.__attack / 2), self.__attack)
        _enemy_health -= int(attack_value * self.type_multiplier())
        if _enemy_health < 0:
            _enemy_health = 0
        return _enemy_health

    def special_attack(self, _enemy_health):
        attack_value = randint(int(self.__attack / 2), int(self.__attack * 1.5))
        _enemy_health -= int(attack_value * self.type_multiplier())
        if _enemy_health < 0:
            _enemy_health = 0
        return _enemy_health

    def heal(self):
        heal_value = randint(20, 40)
        if self.__health + heal_value > self.__max_health:
            self.__health = self.__max_health
            return
        self.__health += heal_value

    def type_multiplier(self):
        match self.__type:
            case 'NORMAL':
                return 1
            case 'FIRE':
                return 1.2
            case 'WATER':
                return 1.2
            case 'ELECTRIC':
                return 1.3
            case 'GRASS':
                return 1.2
            case 'ICE':
                return 1.5
            case 'FIGHTING':
                return 1.3
            case 'POISON':
                return 1.2
            case 'GROUND':
                return 1.3
            case 'FLYING':
                return 1.1
            case 'PSYCHIC':
                return 1.2
            case 'BUG':
                return 1.1
            case 'ROCK':
                return 1.2
            case 'GHOST':
                return 1.4
            case 'DRAGON':
                return 2
            case 'DARK':
                return 1.7
            case 'STEEL':
                return 1.5
            case 'FAIRY':
                return 1.5
            case _:
                return 1

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, _health):
        self.__health = _health

    def get_max_health(self):
        return self.__max_health

    def get_attack(self):
        return self.__attack

    def get_type(self):
        return self.__type
