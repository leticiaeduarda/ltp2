'''1- Crie um projeto usando o conceito de POO com herança (inheritance) contendo a superclasse
   (classe pai) Pessoa e duas subclasses (classes filhas) Professor e Funcionário.
- A superclasse Pessoa tem o atributo de instância nome
- O construtor da superclasse recebe o parâmetro nome e armazena no atributo nome.
- Os métodos get e set referente ao atributo nome. Faça crítica no set
5- A primeira subclasse Professor tem os atributos de instância nome e qtd_turma
- O construtor da subclasse Professor recebe os dois parâmetros e chama o construtor
da superclasse enviado o nome e depois armazena o valor inteiro no atributo qtd_turma.
- Use valor default (padrão) no construtor. Teste
8- Cadastre um professor no sistema, ou seja, crie um objeto da subclasse Professor
9- Use os métodos get e set de nome e qtd de turma
- No método set referente ao atributo qtd_turma, faça pelo menos uma crítica.
11- Cadastre mais um professor passando apenas o nome, teste
12- Crie o método rendimentos, ele recebe o valor em reais que o professor ganha por turma
que ministra e mostra o valor dos seus rendimentos, o objetivo é calcular o rendimento
do professor que depende da quantidade de turmas e do valor que ele ganha por turma.
- E a segunda subclasse Funcionário tem os atributos de instância nome e salario
- O construtor da subclasse Funcionário recebe dois parâmetros e chama o construtor
da superclasse enviando o nome e depois armazena o valor float no atributo salário.
- Use valor default (padrão) no construtor
- No método set referente ao atributo salario, faça uma crítica.
- No main, crie mais um objeto da subclasse Funcionario e use os métodos do sistema
18- O sistema precisa saber quantas pessoas tem cadastrada no sistema.
- Crie o atributo de classe e o método de classe necessários para atender essa necessidade.
- Crie uma lista e adicione todos os objetos instanciados.
- Crie um método de classe para mostrar os dados de todas as pessoas.
'''

import gc


class Pessoa:

    # Inicializando variáveis
    qtd = 0
    instancias = set()

    def __init__(self, nome):
        self.nome = nome
        Pessoa.qtd += 1
        Pessoa.instancias.add(self)

    def get_nome(self):
        return self.nome

    def set_nome(self, nv_nome):
        if type(nv_nome) == str:
            self.nome = nv_nome
        else:
            print(f'- ERRO: {self.set_nome} tipo de dado informado é inválido. :(\nFormato válido deve ser str.')

    @staticmethod
    def get_qtd():
        return Pessoa.qtd

    @classmethod
    def get_instancias(cls):
        return cls.instancias


class Professor(Pessoa):
    def __init__(self, nome, qtd_turma=1):
        super().__init__(nome)
        self.qtd_turma = qtd_turma

    def get_qtd_turma(self):
        return self.qtd_turma

    def set_qtd_turma(self, nv_qtd_turma):
        if isinstance(nv_qtd_turma, int):
            self.qtd_turma = nv_qtd_turma
        else:
            print(f'- ERRO: {self.set_qtd_turma}: o tipo de dado informado é inválido. :(')

    def rendimentos(self):
        valor_turma = float(input("Valor por turma: "))
        valor_total = valor_turma * self.qtd_turma
        print("Quantidade de turmas: ", self.qtd_turma)
        print("Total de rendimentos: ", valor_total)


class Funcionario(Pessoa):
    def __init__(self, nome, salario=2000):
        super().__init__(nome)
        self.salario = salario

    def get_salario(self):
        return self.salario

    def set_salario(self, nv_salario):
        if isinstance(nv_salario, float):
            self.salario = nv_salario
        else:
            print(f'- ERRO: {self.set_salario}: o tipo de dado informado é inválido. :(')


if __name__ == '__main__':

    dados = []

    print('\nQUANTIDADE DE PESSOAS CADASTRADAS:', Pessoa.qtd)
    professor1 = Professor(f'Minerva', 5)
    print('\n*** REGISTRO PROFESSOR ***\nCADASTRO 1:', professor1, '\nNome:', professor1.get_nome(), '\nQuantidade de '
                                                                                                     'turmas:',
          professor1.get_qtd_turma())
    professor1.set_nome('McGonagall')
    professor1.set_qtd_turma(10)
    print('\nCADASTRO 1 ALTERADO\nNovo nome:', professor1.get_nome(), '\nNova quantidade de turmas:',
          professor1.get_qtd_turma())
    print('\nQUANTIDADE DE PESSOAS CADASTRADAS:', Pessoa.qtd)
    funcionario1 = Funcionario(f'Hagrid', 3000)
    print('\n*** REGISTRO FUNCIONÁRIO ***\nCADASTRO 1:', funcionario1, '\nNome:', funcionario1.get_nome(), '\nSalário: '
                                                                                                           'R$',
          funcionario1.get_salario())
    print('\nQUANTIDADE DE PESSOAS CADASTRADAS:', Pessoa.qtd)

    print(f'\n\nTESTE: {Pessoa.instancias}')

'''
    for obj in gc.get_objects():
        if isinstance(obj, Pessoa):
            dados.append(obj)

    print(dados)
'''