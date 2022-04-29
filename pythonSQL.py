import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DNS;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id = 5
cliente = "Lira Python3"
produto = "Carro"
data = '20210825'
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()
print("Valores inseridos")