class Livro:
    def __init__(self, titulo, autores, paginas, preco=0.0):
        self.titulo = titulo
        self.autores = autores
        self.paginas = paginas
        self.preco = preco

    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autores(self):
        return self.autores
    def set_autores(self, n_autores):
        if isinstance(n_autores, list) and len(n_autores) > 0:
            self.autores = n_autores
        else:
            print('- ERRO: O tipo de dado informado é inválido. :(')

#    def mostra_autores(self):
#        print(f'\n-- AUTORES CADASTRADOS:')
#        ct = 0
#        for autor in self.autores:
#           ct +=1
#           print(f'{ct} - {autor}')

    def mostra_autores(self):
        print(f'\n-- AUTORES CADASTRADOS:')
        for i, autor in enumerate(self.autores):
            print(f'{i+1} - {autor}')

    def acrescenta_autor(self, autor):
        self.autores.append(autor)

    def remove_autor(self, autor):
        if autor in self.autores:
            self.autores.remove(autor)
            print(f'Remoção realizada com sucesso! :)')
        else:
            print(f'- ERRO (remove): autor {autor} não está cadastrado.')

    def pesquisa_autor(self, autor):
        if autor in self.autores:
            print(f'Autor {autor} encontrado com sucesso! :)')
        else:
            print(f'Autor {autor} não encontrado... :(')

    def get_paginas(self):
        return self.paginas
    def set_paginas(self, paginas):
        self.paginas = paginas

    def get_preco(self):
        return self.preco
    def set_preco(self, preco):
        self.preco = preco

# Método que calcula o valor do livro pela quantidade de páginas

    def novo_preco(self):
        self.preco = (self.paginas * 0.50)
        return self.preco

# Método que concede desconto porcentual

    def desconto(self):
        self.preco = (self.preco - self.preco * 0.1)
        return self.preco

if __name__ == '__main__':

    livro1 = Livro(f'Harry Potter', 'JK Rowling', 322, 100)
    print(f'\nAutor(es) Cadastro 1:', livro1.get_autores())
    livro1.set_autores(['JK Rowling', 'Hermione'])
    print(f'\nAutor(es) atualizados Cadastro 1:', livro1.get_autores()[0], 'e', livro1.get_autores()[1])
    livro2 = Livro(f'Senhor dos Anéis', ['J. R. R. Tolkien'], 521, 200)

    livro1.novo_preco()
    livro2.novo_preco()

    livro1.mostra_autores()
    livro2.mostra_autores()

    print(f"\n*** CADASTRO 1 ***\nTítulo: {livro1.titulo}\nAutor(es): {livro1.autores[0]} e {livro1.autores[1]} \nPáginas: {livro1.paginas}"
    f"\nPreço: R${livro1.desconto()}\n"
    f"\n*** CADASTRO 2 ***\nTítulo: {livro2.titulo}\nAutor(es): {livro2.autores[0]} \nPáginas: {livro2.paginas}"
    f"\nPreço: R${livro2.desconto()}\n")