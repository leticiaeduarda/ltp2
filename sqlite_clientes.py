# Letícia Eduarda Alve
# RA: 22100122

#  ATIVIDADE 2

# 1. Desenvolva um programa em Python e crie uma base de dados:
#     -crie uma tabela com uma chave primária
#     -crie pelo menos uma coluna obrigatória
#     -crie pelo menos uma coluna opcional.

# 2. Implemente um programa em Python para inserir dados na tabela criada.

# 3. Faça um programa em Python para consultar os registros inseridos na tabela criada. Mostre os registros na vertical

# Obs.: crie uma tabela e colunas diferentes das desenvolvidas nas aulas.

import sqlite3

# conectar
conexao = sqlite3.connect('clientes_db')

# criar o cursor
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE tb_cliente(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cliente VARCHAR(30) NOT NULL,
        nascimento DATE NULL,
        endereco VARCHAR(50) NULL)
        ''')

# verificar tabela criada
# cursor.execute('''
# SELECT * FROM tb_cliente
#         ''')
#
# for coluna in cursor.description:
#     print(coluna[0])

# inserir dados na tabela
cursor.execute('''
INSERT INTO tb_cliente (cliente, nascimento, endereco)
values
('Matheus', '1997-03-30', 'Águas Claras Lote 10'),
('Flavio', '1994-12-06', 'Areal Rua 06 Casa 02')
''')

# salvar no banco
conexao.commit()

v_cliente = input('\n***** CADASTRE UM NOVO CLIENTE *****\nNome do Cliente: ')  # Recebe dados
v_nascimento = input('Data de nascimento (aaaa-mm-dd)(opcional): ')
v_endereco = input('Endereço (opcional): ')

cursor.execute(('''
INSERT INTO tb_cliente (cliente, nascimento, endereco)
values
(?, ?, ?)
'''), (v_cliente, v_nascimento, v_endereco))

cursor.execute('''
SELECT * FROM tb_cliente
        ''')


def mostra_cliente(cursor):
    print('\n***** CLIENTES CADASTRADOS *****')
    # for row in cursor:
    #     print(row)
    for col in cursor:
        print(f'Cliente: {col[0]}\nNome: {col[1]}\nData de nascimento: {col[2]}\nEndereço: {col[3]}\n')


mostra_cliente(cursor)

# encerrar conexao
conexao.close()
