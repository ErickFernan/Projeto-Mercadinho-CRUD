import mysql.connector  # Comando para fazer a ligação: pip3 install mysql-connector-python


def conectar(login, senha):
    """
    Função para conectar ao servidor
    """
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