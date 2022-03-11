import mysql.connector  # Comando para fazer a ligação: pip3 install mysql-connector-python
import re


def conectar(login, senha):
    """"""
    try:
        conn = mysql.connector.connect(
            db='mercadinho',
            host='localhost',
            user=f'{login}',
            passwd=f'{senha}'
        )
        return conn
    except mysql.connector.Error as e:
        print(f'Erro na conexão ao MySQL Server {e}')


def desconectar(conn):
    """"""
    if conn:
        conn.close()


def mostra_tabelas(conn):
    """"""
    cursor = conn.cursor()
    cursor.execute('SHOW TABLES')
    tabelas = cursor.fetchall()

    if len(tabelas) > 0:
        print('Listando tabelas:-----')
        print('----------------------')
        print('Nome da tabela | Opção')
        for n, tabela in enumerate(tabelas):
            tabela = str(tabela)
            new_string = re.sub(r"[^a-zA-Z0-9]", "", tabela)
            print(f'{new_string:<14} | {n:^5}')
        print('')

        # LEMBRAR DE FORMATAR PARA FICAR BONITO


def escolhe_acao_crud():
    """"""
    acao = input("""
Escolha o que deseja fazer:
[1] Ler dados da tabela
[2] Inserir dados na tabela
[3] Modificar dados da tabela
[4] Deletar a tabela
""")
    return acao


def listar(conn, nome):
    """"""
    cursor = conn.cursor()  # Necessário para acessar o banco de dados
    cursor.execute(f'SELECT * FROM {nome}')  # Executa o comando SQL
    itens = cursor.fetchall()  # Pega o resultado da linha anterior e transforma em uma lista

    # Verificando se a lista está vazia
    if len(itens) > 0:
        print('Listando produtos...')
        print('--------------------')
        print(itens)
        for item in itens:
            print(item)
            print('--------------------')
    else:
        print('Não existem produtos cadastrados.')


# def inserir():
#     """"""
#     conn = conectar()
#     cursor = conn.cursor()
#
#     nome = input('Informe o nome do protudo: ')
#     preco = float(input('Informe o preço do protudo: '))
#     estoque = int(input('Informe o estoque do protudo: '))
#
#     cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
#     conn.commit()
#
#     if cursor.rowcount == 1:  # rowcount -> contagem de linhas
#         print(f'O produto {nome} foi inserido com sucesso.')
#     else:
#         print('Não foi possível inserir o produto.')
#
#     desconectar(conn)
#
#
# def atualizar():
#     """"""
#     conn = conectar()
#     cursor = conn.cursor()
#
#     codigo = int(input('Escreva o código do produto: '))
#     nome = input('Informe o novo nome do produto: ')
#     preco = float(input('Informe o novo preço do produto: '))
#     estoque = int(input('Informe a nova quantidade em estoque: '))
#
#     cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
#     conn.commit()
#
#     if cursor.rowcount == 1:  # rowcount -> contagem de linhas
#         print(f'O produto {nome} foi atualizado com sucesso.')
#     else:
#         print('Não foi possível atualizar o produto.')
#
#     desconectar(conn)
#
#
# def deletar():
#     """"""
#     conn = conectar()
#     cursor = conn.cursor()
#
#     codigo = int(input('Qual o código do produto a ser deletado? '))
#
#     cursor.execute(f'DELETE FROM produtos WHERE id = {codigo}')
#     conn.commit()
#
#     if cursor.rowcount == 1:  # se ele conseguiu deletar um cara ele retorna 1
#         print('Produto excluído com sucesso.')
#     else:
#         print(f'Erro ao excluir o produto com id = {codigo}.')
#
#     desconectar(conn)
