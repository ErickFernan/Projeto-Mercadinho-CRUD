from lib.interface import *
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
    nome_tabelas = []
    cursor = conn.cursor()
    cursor.execute('SHOW TABLES')
    tabelas = cursor.fetchall()

    if len(tabelas) > 0:
        print('Listando tabelas:')
        print('----------------------')
        print('Nome da tabela | Opção')
        for n, tabela in enumerate(tabelas):
            tabela = str(tabela)
            new_string = re.sub(r"[^a-zA-Z0-9]", "", tabela)
            nome_tabelas.append(new_string)
            print(f'{new_string:<14} | {n:^5}')
        print('')
        opc = int(input('Escolha a tabela que deseja editar: '))
        return str(nome_tabelas[opc])


def executa_acao(conn, nome, operacao):
    """"""
    if operacao == '1':
        listar(conn, nome)
    if operacao == '2':
        inserir(conn, nome)


def pega_titulo_tabela(conn, nome):
    """"""
    nome_tabelas = []
    cursor = conn.cursor()
    cursor.execute(f'DESC {nome}')
    tabelas_titulo = cursor.fetchall()
    for titulo in tabelas_titulo:
        nome_tabelas.append(titulo[0])

    return nome_tabelas


def listar(conn, nome):
    """"""
    cursor = conn.cursor()  # Necessário para acessar o banco de dados
    cursor.execute(f'SELECT * FROM {nome}')  # Executa o comando SQL
    itens = cursor.fetchall()  # Pega o resultado da linha anterior e transforma em uma lista

    # Verificando se a lista está vazia
    if len(itens) > 0:
        print('Listando produtos...')
        titulo_tabela = pega_titulo_tabela(conn, nome)
        print('-' * 26 * len(titulo_tabela))
        for palavra in titulo_tabela:
            print(f'{ palavra:^24} |', end='')
        print('')
        for item in itens:
            for valor in item:
                print(f'{valor:^24} |', end='')
            print('')
        print('-' * 26 * len(titulo_tabela))
    else:
        print('Não existem produtos cadastrados.')


def inserir(conn, nome):
    """"""
    valores_tab = list()
    cursor = conn.cursor()
    titulo_tabela = pega_titulo_tabela(conn, nome)

    for c in range(len(titulo_tabela)-1):  # Menos 1 pois o id é auto incremento
        valores_tab.append(input(f'Informe o {titulo_tabela[c+1]}: '))

    cursor.execute(f"INSERT INTO {nome} ({re.sub(r'[^a-zA-Z0-9,]', '', str(titulo_tabela[1:]))}) "
                   f"VALUES ({(str(valores_tab)).replace(']','').replace('[','')})")

    conn.commit()

    if cursor.rowcount >= 1:  # rowcount -> contagem de linhas
        print(f'Os dados foram inseridos com sucesso.')
    else:
        print('Não foi possível inserir os dados.')


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
