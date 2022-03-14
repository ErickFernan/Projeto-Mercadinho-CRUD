from lib.Arquivo import *


def conexao():
    """"""
    while True:
        login = input('Digite seu nome de usuário: ')
        senha = input('Digite sua Senha: ')

        conn = conectar(login, senha)

        if conn:
            print('Conexão feita com sucesso!\n')
            return conn


def escolhe_acao():
    """"""
    while True:
        acao = input("""
[1] Ler dados da tabela
[2] Inserir dados na tabela
[3] Modificar dados da tabela
[4] Deletar compo de uma tabela
Escolha o que deseja fazer: """)
        ans = input(f'Voce escolheu a ação {acao}, está certo disso? [S/N]\n').upper().strip()[0]
        if ans in ['S']:
            return acao


def primeira_acao(conn):
    """"""
    print("""[1] Editar tabelas
[2] Ver resumo de uma compra""")
    ans = input('Escolha sua ação: ')
    if ans == '1':
        nome = mostra_tabelas(conn)

        operacao = escolhe_acao()

        executa_acao(conn, nome, operacao)

    elif ans == '2':
        info_imprime_nota(conn)
