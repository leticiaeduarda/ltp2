# - Atividade individual 1
#
# - Prazo: 10/04, até 23h59
#
# - Envio:
# Crie um único arquivo.py com o seu primeironome, o caractere underline e o segundonome.
# Exemplo: antonio_vitor.py
#
#
# - Resolva o exercício usando a linguagem Python e os conceitos de POO com herança e classe abstrata.
#
#
# - Exercícios:
#
# 1. Crie pelo menos três classes com seus respectivos atributos e métodos.
#
# 2. Uma das classes criadas deve ser classe abstrata e pelo menos um método abstrato.
#
# 3. No main, crie pelo menos um objeto de cada classe e use (teste) todos os métodos das três classes.
#
#
# Obs.: crie as classes e os métodos diferentes dos desenvolvidos durante as aulas.

from abc import ABC, abstractmethod


class Pokemon(ABC):

    def __init__(self, nome):
        self.nome = nome


    @abstractmethod
    def ataque(self):
        ...

    @property
    @abstractmethod
    def level(self):
        ...

    @property
    @abstractmethod
    def tipo(self):
        ...

    @property
    @abstractmethod
    def pokedex(self):
        ...


class Pikachu(Pokemon):
    def ataque(self):
        return f'{self.nome} usou Choque do Trovão! O dano causado foi 15.'

    @property
    def level(self):
        return 1

    @property
    def tipo(self):
        return 'Elétrico'

    @property
    def pokedex(self):
        return 'Pikachu que pode gerar eletricidade poderosa tem bolsas nas bochechas que são extra macias e super' \
               ' elásticas. Evolução do Pichu e pré-evolução do Raichu.'


class Charmander(Pokemon):
    def ataque(self):
        return f'{self.nome} usou Presas de Fogo! O dano causado foi 10.'

    @property
    def level(self):
        return 1

    @property
    def tipo(self):
        return 'Fogo'

    @property
    def pokedex(self):
        return 'É um Pokémon inicial. Tem preferência por coisas quentes. Quando chove, diz-se que o vapor jorra da' \
               ' ponta de sua cauda. Suas evoluções são Charmeleon e Charizard.'


class Squirtle(Pokemon):
    def ataque(self):
        return f'{self.nome} usou Rajada de Bolhas! O dano causado foi 12.'

    @property
    def level(self):
        return 1

    @property
    def tipo(self):
        return 'Água'

    @property
    def pokedex(self):
        return 'É um Pokémon inicial. Quando retrai seu longo pescoço em sua concha, esguicha água com força vigorosa.'\
               ' Suas evoluções são Wartortle e Blastoise.'


class Bulbasaur(Pokemon):
    def ataque(self):
        return f'{self.nome} usou Folha Navalha! O dano causado foi 9.'

    @property
    def level(self):
        return 1

    @property
    def tipo(self):
        return 'Planta'

    @property
    def pokedex(self):
        return 'É um Pokémon inicial. Há uma semente de planta nas costas desde o dia em que este Pokémon nasce. A ' \
               'semente cresce lentamente. Suas evoluções são Ivysaur e Venusaur.'


if __name__ == '__main__':

    charmander1 = Charmander('Dark Charmander')
    pikachu1 = Pikachu('Whisky Pikachu')
    squirtle1 = Squirtle('Tortuga Squirtle')
    bulbasaur1 = Bulbasaur('TK Bulbasaur')

    print(f'\n***BATALHA 1***\n\nPlayer 1:\n- {charmander1.nome} eu escolho você!\n\n***POKÉDEX***\n'
          f'{charmander1.__class__.__name__}...\n{charmander1.pokedex}\nTIPO: {charmander1.tipo}')
    print(f'\nPlayer 2:\n- {pikachu1.nome} eu escolho você!\n\n***POKÉDEX***\n{pikachu1.__class__.__name__}...\n'
          f'{pikachu1.pokedex}\nTIPO: {pikachu1.tipo}')
    print(f'\n*** {charmander1.nome} LV.{charmander1.level} x {pikachu1.nome} LV.{pikachu1.level} ***')
    print(f'\n{charmander1.ataque()}\n{pikachu1.ataque()}')
    print(f'\n{pikachu1.nome} vence a batalha!')

    print(f'\n***BATALHA 2***\n\nPlayer 1:\n- {squirtle1.nome} eu escolho você!\n\n***POKÉDEX***\n'
          f'{squirtle1.__class__.__name__}...\n{squirtle1.pokedex}\nTIPO: {squirtle1.tipo}')
    print(f'\nPlayer 2:\n- {bulbasaur1.nome} eu escolho você!\n\n***POKÉDEX***\n{bulbasaur1.__class__.__name__}...\n'
          f'{bulbasaur1.pokedex}\nTIPO: {bulbasaur1.tipo}')
    print(f'\n*** {squirtle1.nome} LV.{squirtle1.level} x {bulbasaur1.nome} LV.{bulbasaur1.level} ***')
    print(f'\n{squirtle1.ataque()}\n{bulbasaur1.ataque()}')
    print(f'\n{squirtle1.nome} vence a batalha!')

