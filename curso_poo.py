# 2. Modele a classe Curso com os atributos nome do curso, valor do curso e os alunos. Usando o conceito de associação
# de classes, o atributo alunos da classe Curso deve ser os objetos da classe Aluno. Lembrando que um curso pode ter
# vários alunos.
#
# Implemente a classe Curso com o construtor, os métodos gets e sets necessários e estes métodos funcionais dentro da
# classe Curso:
# - insere_aluno, ele inclui um aluno no curso;
# - mostra_dados_curso, ele mostra todos os dados do curso;
#
# - consulta_nome_alunos, ele mostra a relação com o nome de todos os alunos do curso.
#
# E a classe Aluno tem os atributos ra do aluno e nome do aluno. Implemente a classe Aluno com o construtor, e pelo
# menos um método gets e um método set.
#
# No método main, crie dois objetos da classe aluno e pelo menos um objetos da classe Curso. Em cada curso cadastre
# alguns alunos. E teste todos os métodos desenvolvidos.


class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome

    def get_ra(self):
        return self.ra

    def set_ra(self, ra):
        self.ra = ra

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome


class Curso:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.alunos = list()

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def insere_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostra_dados_curso(self):
        print(f'\n*** DADOS DO CURSO: ***\nNome: {self.nome}\nValor: R${self.valor}\n')

    def consulta_nome_alunos(self):
        if not self.alunos:
            print('A lista está vazia.')
        else:
            print('Relação dos alunos do curso:')
            for o_aluno in self.alunos:
                print(o_aluno.get_nome())


if __name__ == '__main__':

    # cadastro alunos
    aluno1 = Aluno("65163516", "Aline")
    aluno2 = Aluno("16541663", "Bianca")
    aluno3 = Aluno("65416314", "João")
    # cadastro de cursos
    curso1 = Curso("Computação", 900)
    curso2 = Curso("Engenharia", 1200)
    # insere alunos no curso
    curso1.insere_aluno(aluno1)
    curso1.insere_aluno(aluno2)
    curso1.insere_aluno(aluno3)
    aluno4 = Aluno("23665436", "Maria")
    aluno5 = Aluno("64165464", "Pedro")
    aluno6 = Aluno("59647347", "Sabrina")
    curso2.insere_aluno(aluno4)
    curso2.insere_aluno(aluno5)
    curso2.insere_aluno(aluno6)
    # teste dos métodos
    curso1.mostra_dados_curso()
    curso1.consulta_nome_alunos()
    curso2.mostra_dados_curso()
    curso2.consulta_nome_alunos()
