from lib.Arquivo import *


def conexao():
    while True:
        login = input('Digite seu nome de usuário: ')
        senha = input('Digite sua Senha: ')

        conn = conectar(login, senha)

        if conn:
            print('Conexão feita com sucesso!\n')
            return conn


def escolhe_tabela(conn):
    mostra_tabelas(conn)
    nome = input('Escolha a tabela que deseja editar: ')
    return nome


def escolhe_acao():
    while True:
        acao = escolhe_acao_crud()
        ans = input(f'Voce escolheu a ação {acao}, está certo disso? [S/N]\n').upper().strip()[0]
        if ans in ['S']:
            return ans
