import getpass
from lib.Arquivo import *


def conexao():
    while True:
        login = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')

        conn = conectar(login, senha)

        if conn:
            print('Conexão feita com sucesso!')
            break