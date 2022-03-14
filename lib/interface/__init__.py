from lib.Arquivo import *


def detalhes_compra():
    """"""
    print('cheguei aqui DC')
    # dados_cli, id_compra, compras = info_imprime_nota(conn)
    # print(dados_cli)
    # print(id_compra)
    # print(compras)


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
[5] Imprimir detalhes de uma compra
Escolha o que deseja fazer: """)
        ans = input(f'Voce escolheu a ação {acao}, está certo disso? [S/N]\n').upper().strip()[0]
        if ans in ['S']:
            return acao
