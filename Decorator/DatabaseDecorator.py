import pyodbc


def conexao(dados_conexao):
    try:
        global conecta
        conecta = pyodbc.connect(dados_conexao)
        print('OK! conexao estabelecida')
        return True
    except Exception as e:
        print('Não foi possível conectar no banco de dados. Abortando.')
        print(e)
        responseStatus = 599
        return False


def finalizaConexao():
    conecta.close()
    print('Conexão finalizada')


def queryUnica(query):
    try:
        cursor = conecta.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        return row
    except Exception as e:
        responseStatus = 409
        raise


def database_connection_decorator(dados_conexao):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                conexao(dados_conexao)
                result = func(*args, **kwargs)
            finally:
                finalizaConexao()

            return result
        return wrapper
    return decorator
