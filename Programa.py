from lib.interface import *
from lib.Arquivo import *

conn = conexao()

nome = mostra_tabelas(conn)

operacao = escolhe_acao()

executa_acao(conn, nome, operacao)

