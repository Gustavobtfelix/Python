import pyodbc
#Cria conexao com o banco de dados
def conexao(dados_conexao):
    try:
        global conecta
        conecta = pyodbc.connect(dados_conexao)
        print('OK! conexao estabelecida')
        return True
    except Exception as e:
        print('Não foi possível conectar no banco de dados.')
        print(e)
        return False

#Finaliza conexao com o banco de dados
def finalizaConexao():
    conecta.close()
    print('Conexão finalizada')

#Decorator banco de dados: Acessa banco de dados > Executa query > Retorna resultado
def acessaDatabase(function):
    def wrapper(*args):
        argumentos = args[0]
        print(argumentos)
        try:
            if conexao(argumentos['dados']):
                result = function(argumentos['query'], argumentos['parameters'])
                finalizaConexao()
                # result vai ser o resultado da query ou None se não encontrar
                return result
            else:
                #falha ao conectar com banco
                return None
        except Exception as e:
            #para erros causados por query mal formada
            finalizaConexao()
            return None
    return wrapper

#Faz a busca de multiplos dados no banco de dados
@acessaDatabase
def buscaDadosMultiplos(query, parameters):
    try:
        result_list = []
        cursor = conecta.cursor()
        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        if rows is None:
            print("nenhum dado encontrado")
        else:
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

#Faz a busca de um dado no banco de dados
@acessaDatabase
def buscaDadoUnico(query, parameters):
    try:
        result_list = {}
        cursor = conecta.cursor()
        if(parameters is None):
            cursor.execute(query)
        else:
            cursor.execute(query, parameters)
        row = cursor.fetchone()
        if row is None:
            print("nenhum dado encontrado")
        else: 
            for idx, column in enumerate(cursor.description):
                column_name = column[0]
                result_list[column_name] = row[idx]
            return result_list
        return row
    except Exception as e:
        print('erro ao executar query unica')
        print(e)
        raise

#Faz Insert ou update
@acessaDatabase
def alteraInformacoes(query, parameters):
    try:
        cursor = conecta.cursor()
        if(parameters is None):
            cursor.execute(query)
        else:
            cursor.execute(query, parameters)
        conecta.commit()
        return True
    except Exception as e:
        print('erro ao executar query unica')
        print(e)
        raise
    
if __name__ == '__main__':
    
    conexao_dados  = (
    "Driver={SQL Server};"
    "Server=00.00.000.000;"
    "Database=YourDatabase;"
    "Username = user;"
    "Password = yourPassword"
    )
    
    query = "SELECT top(1) * FROM your_database where cpf = ?"
    parameters = ["000.000.000-00"]
    dicionario = {'dados': conexao_dados, 'query': query, 'parameters':parameters}
    resultado = buscaDadoUnico(dicionario)
    # resultado= buscaDadosMultiplos(dicionario)
    if(resultado is None):
        print('erro')
    else:
        print(resultado)
    
    # query = "SELECT * FROM your_database WHERE cpf IN ({})".format(','.join(['?'] * len(parameters)))