import pyodbc
import sys
import time

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DNS;"
    "Database=PythonSQL;"
)
#"UID=user"
#"PWD=senha"
#Username=user
#Password=senha


def conexao():
    try:
        global conecta
        conecta = pyodbc.connect(dados_conexao)
        print ('OK! conexao estabelecida')
        return True
    except Exception as e:
        print ('Não foi possível conectar no banco de dados. Abortando.')
        print(e)
        sys.exit(1)

def finalizaConexao():
    conecta.close()
    print ('Conexão finalizada')

        
def buscaDados():

    cursor = conecta.cursor()
    #dt_server(datetime), ticket(nvarchar(50)), nome(nvarchar(250)), cpf(nvarchar(14)), empresa(nvarchar(50)), local_trabalho(nvarchar(250)), dt_welcome(date) 
    try:
        comando = f"""
        select *
        from Vendas"""

        cursor.execute(comando)
        print("OK, consulta realizada")
        rows = cursor.fetchall()
        return rows
    
    except Exception as e:
        print ('ERRO NA CONSULTA:')
        print (e)
        sys.exit(1)


comando = f""""""

cursor.execute(comando)
cursor.commit()
print("Valores inseridos")

 

if(__name__ == "__main__"):
    start_time = time.time()
    conexao()
    dados = buscaDados()
    print (dados.__len__())

    print("--- %s seconds ---" % (time.time() - start_time))

    finalizaConexao()