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
        return False


def finalizaConexao():
    conecta.close()
    print('Conexão finalizada')


def acessaDatabase(function):
    def wrapper(*args):
        argumentos = args[0]
        try:
            if conexao(argumentos['dados']):
                result = function(argumentos['query'])
                finalizaConexao()
                return result
            else:
                pass
        except Exception as e:
            finalizaConexao()
    return wrapper

@acessaDatabase
def buscaDadosMultiplos(query):
    try:
        result_list = []
        cursor = conecta.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        # Assuming 'cursor.description' contains column names
        column_names = [desc[0] for desc in cursor.description]

        for row in rows:
            row_dict = {col_name: value for col_name, value in zip(column_names, row)}
            result_list.append(row_dict)

        return result_list     
    except Exception as e:
        print('erro ao executar query multipla')
        print(e)
        raise

@acessaDatabase
def buscaDadoUnico(query):
    try:
        result_list = {}
        cursor = conecta.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row: 
            for idx, column in enumerate(cursor.description):
                column_name = column[0]
                result_list[column_name] = row[idx]
            return result_list
        return row
    except Exception as e:
        print('erro ao executar query unica')
        print(e)
        raise
    
if __name__ == '__main__':
    
    conexao_dados  = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=00.000.000.00;"
        "Database=your_database;"
        "UID=user;" # usuario
        "PWD=password" # password
    )
    
    query = "SELECT * FROM your_table"
    dicionario = {'dados': conexao_dados, 'query': query}
    resultado = buscaDadosMultiplos(dicionario)
    
    print(resultado[0]['nome_coluna'])

