from lib.interface import *
from lib.Arquivo import *

conn = conexao()

while True:
    primeira_acao(conn)

    ans = input('Deseja fazer outra operação? [S/N] ').upper().strip()[0]

    if ans not in ['S']:
        desconectar(conn)
        print('Operação encerrada com sucesso!')
        break
