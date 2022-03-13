from lib.interface import *
from lib.Arquivo import *

conn = conexao()

while True:

    nome = mostra_tabelas(conn)

    operacao = escolhe_acao()

    executa_acao(conn, nome, operacao)

    ans = input('Deseja fazer outra operação? [S/N] ').upper().strip()[0]

    if ans not in ['S']:
        desconectar(conn)
        break
