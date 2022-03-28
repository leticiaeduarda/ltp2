# - Usando o conceito de associação de classes em POO, faça a análise das classes
# necessárias para desenvolva um sistema de carrinho de compras com as informações
# do pedido, do cliente e dos produtos colocados no carrinho.
#
# Implemente:
# 1- Crie a classe Cliente com os atributos (características) cpf e nome ok
# - Crie os métodos gets, teste. ok
# - Crie a classe CarrinhoCompra com os atributos número do pedido, o cliente e os produtos. ok
# - Crie os métodos gets, teste ok
# 5- Crie a classe Produto com os atributos: identificador, nome, preço e quantidade. ok
# - Crie os métodos gets, teste ok
# - Crie o método __str__ pra retornar todos os dados de um produto formatados (concatenados)
# 8- Crie o método mostra carrinho, teste ok
# - Insira um produto no carrinho de compras do cliente1. Crie o método insere_produto, ok
# ele recebe um objeto da classe Produto e insere no carrinho.
# 10- Insira mais um produto no carrinho de compras do cliente1, teste
# - Crie o método mostra_carrinho2, com todos os dados do produto e a quantidade de itens
# no carrinho. Se o carrinho estiver vazio, mostre a mensagem "Carrinho vazio". Teste
# - Crie o método retorna_total, ele calcula e retorna o valor total da compra,
# ou seja, dos produtos no carrinho de compras, teste  (valor total 57,00)
# 13- Crie o método remova_produto, ele remove um produto do carrinho de compras, teste
# - Crie o método remova_produto2, ele remove um produto do carrinho de compras
#   com críticas e mensagens, teste
# 15- Insira mais um produto no carrinho de compras do cliente1, teste
# - Crie o método fecha_compra. Ele finalize a compra e mostra os produtos e o
#   valor total, teste
# 17- Crie o método remova_produto3, ele não recebe nada, mostre todos os produtos no carrinho,
#   o cliente escolhe o produto para remover e remove o produto do carrinho de compras, teste
# - Finalize a compra e feche o carrinho 2. Além de mostrar os produtos e o valor total
#   Mostrar também o número de pedido, o nome do cliente, a data e hora, teste

class Cliente:
    def __init__(self, cpf, nome=''):
        self.cpf = cpf
        self.nome = nome

    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome

class CarrinhoCompra:
    def __init__(self, n_pedido, o_cliente):
        self.n_pedido = n_pedido
        self.cliente = o_cliente                  # objeto da classe cleinte
        self.produtos = list()                    # self.produtos = []

    def get_n_pedido(self):
        return self.n_pedido

    def get_cliente_nome(self):                   # Redundante, não precisa
        return self.cliente.get_nome()

    def mostra_carrinho(self):
        print('\n- Mostra carrinho:')
        for o_produto in self.produtos:
            print('Descrição:', o_produto.get_nome())

    def mostra_carrinho2(self):
        qtd = len(self.produtos)
        if not self.produtos:                     # if self.produtos == []
            print('Carrinho vazio.')
        else:
            print('\n- Mostra carrinho 2:')
            for o_produto in self.produtos:
                print(o_produto)                  # print(o_produto.__str__())
            print('Quantidade de itens:', qtd)

    def insere_produto(self, o_produto):
        self.produtos.append(o_produto)

class Produto(object):
    def __init__(self, idt, nome, preco=0.0, qtd=1):
        self.idt = idt
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_qtd(self):
        return self.qtd

    def __str__(self):
        dados = f'Idt: {self.idt}, Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.qtd}'
        return dados

if __name__ == '__main__':

    cliente1 = Cliente(123)
    print(cliente1)
    cliente2 = Cliente(224, 'Ailton')
    print(cliente2)
    carrinho1 = CarrinhoCompra(12, cliente2)
    print('\nNúmero:', carrinho1.get_n_pedido(), '\nNome:', carrinho1.get_cliente_nome())
    p1_arroz = Produto(1, 'Arroz', 30.0)
    print(p1_arroz)
    carrinho1.mostra_carrinho()
    carrinho1.insere_produto(p1_arroz)
    carrinho1.mostra_carrinho()
    p2_feijao = Produto(2, 'Feijão', 9.00, 3)
    carrinho1.insere_produto(p2_feijao)
    carrinho1.mostra_carrinho2()