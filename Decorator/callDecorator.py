from DatabaseDecorator import database_connection_decorator

dados_conexao = "your_connection_string_here"


@database_connection_decorator(dados_conexao)
def fetch_data_from_database():
    query = "SELECT * FROM your_table"
    row = queryUnica(query)
    return row


result = fetch_data_from_database()
print(result)
