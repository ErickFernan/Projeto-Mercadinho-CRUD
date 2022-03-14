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
    elif operacao == '2':
        inserir(conn, nome)
    elif operacao == '3':
        atualizar(conn, nome)
    elif operacao == '4':
        deletar(conn, nome)


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
                print(f'{str(valor):^24} |', end='')
            print('')
        print('-' * 26 * len(titulo_tabela))
    else:
        print('Não existem produtos cadastrados.')


def inserir(conn, nome):
    """"""
    valores_tab = list()
    cursor = conn.cursor()
    titulo_tabela = pega_titulo_tabela(conn, nome)

    try:
        for c in range(len(titulo_tabela)-1):  # Menos 1 pois o id é auto incremento
            valores_tab.append(input(f'Informe o {titulo_tabela[c+1]}: '))

        cursor.execute(f"INSERT INTO {nome} ({re.sub(r'[^a-zA-Z0-9,_]', '', str(titulo_tabela[1:]))}) "
                       f"VALUES ({(str(valores_tab)).replace(']','').replace('[','')})")

        conn.commit()

        if cursor.rowcount >= 1:  # rowcount -> contagem de linhas
            print(f'Os dados foram inseridos com sucesso.')
    except mysql.connector.Error as e:
        print(f'Não foi possível inserir os dados: {e}')


def atualizar(conn, nome):
    """"""
    txt = []
    valores_tab = list()
    cursor = conn.cursor()  # Necessário para acessar o banco de dados
    titulo_tabela = pega_titulo_tabela(conn, nome)
    _id = int(input('Escreva o ID a ser atualizado: '))

    try:
        for c in range(len(titulo_tabela) - 1):  # Menos 1 pois o id é auto incremento
            valores_tab.append(input(f'Informe o {titulo_tabela[c + 1]}: '))

        # Criando o texto que irá para o comando SQL
        for v in range(len(valores_tab)):
            txt.append(f"{titulo_tabela[v+1]} = '{valores_tab[v]}',")

        texto = " ".join(txt)[:-1]

        cursor.execute(f"""UPDATE {nome} SET
        {texto}
        WHERE id={_id}""")

        conn.commit()

        if cursor.rowcount >= 1:  # rowcount -> contagem de linhas
            print(f'Os dados foram atualizados com sucesso.')
    except mysql.connector.Error as e:
        print(f'Não foi possível atualizar os dados: {e}')


def deletar(conn, nome):
    """"""
    cursor = conn.cursor()  # Necessário para acessar o banco de dados

    codigo = int(input('Qual o ID a ser deletado? '))
    try:
        cursor.execute(f'DELETE FROM {nome} WHERE id = {codigo}')
        conn.commit()

        if cursor.rowcount >= 1:  # se ele conseguiu deletar um cara ele retorna 1
            print('Dado excluído com sucesso.')

    except mysql.connector.Error as e:
        print(f'Não foi possível excluir os dados: {e}')


def info_imprime_nota(conn):
    """"""
    _id = input('Digite o id do cliente: ')
    cursor = conn.cursor()  # Necessário para acessar o banco de dados
    cursor.execute(f'SELECT * FROM clientes WHERE id = {_id}')  # Executa o comando SQL
    dados_cli = cursor.fetchall()  # Pega o resultado da linha anterior e transforma em uma lista

    cursor.execute(f"SELECT data,id FROM compras WHERE id_cliente ='{_id}'")  # Executa o comando SQL
    data_info = cursor.fetchall()  # Pega o resultado da linha anterior e transforma em uma lista
    print(f"{'DATA':^20}|{'ID COMPRA':^20}")
    for i in range(len(data_info)):
        print(f"{str(data_info[i][0]):^20}|{data_info[i][1]:^20}")

    id_compra = input('Selecione o id da compra: ')
    cursor.execute(f"""SELECT p.produto, p.preco_venda , tp. produto, f.nome, lp.quantidade
FROM produtos AS p, tiposproduto AS tp, fabricantes AS f, listaprodutos AS lp, compras as com
WHERE p.id_fabricantes = f.id AND p.id_tipo = tp.id AND lp.id_produto = p.id AND com.id = lp.id_compras 
AND lp.id_compras = {id_compra}""")  # Executa o comando SQL
    compras = cursor.fetchall()

    cursor.execute(f"SELECT data FROM compras WHERE id = {id_compra}")
    data = cursor.fetchall()

    print(f"{'-' * 77}\n{'DETALHES DA COMPRA':^77}\n{'-' * 77}")
    print(f"""
{'NOME:':<10}{dados_cli[0][1]:<26}{'ENDEREÇO:':<10}{dados_cli[0][2]:<26}
{'TELEFONE:':<10}{dados_cli[0][3]:<26}{'CEP:':<10}{dados_cli[0][4]:<26}
{'CIDADE:':<10}{dados_cli[0][5]:<26}{'CPF:':<10}{dados_cli[0][6]:<26}
{'DATA:':<10}{data[0][0]}
{'-'*77}
{'PEDIDOS':^77}
{'-'*77}
{'PRODUTO':^15}|{'PREÇO':^15}|{'TIPO':^15}|{'FABRICANTE':^15}|{'QUANTIDADE':^15}""")
    for item in compras:
        print(f"{item[0]:^15}|{item[1]:^15}|{item[2]:^15}|{item[3]:^15}|{item[4]:^15}")
    print('')
