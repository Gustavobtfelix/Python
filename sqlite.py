import sqlite3
from datetime import datetime, timedelta, time

# define connection and cursor

connection = sqlite3.connect('registroWelcome.db')

cursor = connection.cursor()

# cria tabela caso ela não exista

command1 = """ CREATE TABLE IF NOT EXISTS dadosWelcome (
dt_server TEXT,
ticket TEXT,
nome TEXT,
cpf TEXT PRIMARY KEY,
empresa TEXT,
local_trabalho TEXT,
dt_welcome TEXT )
"""
cursor.execute(command1)
connection.commit()

#Buscando dados SQLite
cursor.execute("select dt_server, cpf, dt_welcome from dadosWelcome")
dadosSQLite = cursor.fetchall()

# #Buscando dados SQL Server
# querySQL.conexao()
# dadosBanco = querySQL.buscaDados()

# #busca dados SQLite e base LG
# dadosLGSQLite = querySQL.buscaDados2(dadosSQLite)


# print ("Colaboradores na base welcome: " + str(dadosBanco.__len__()))
print ("Colaboradores banco SQLite: " + str(dadosSQLite.__len__()))
# print("Colaboradores na SQLite e LG: " +str(dadosLGSQLite.__len__()))

#Verificando se há novos colaboradores

# n = 1
# encontrou = False
# for dados in dadosBanco:
#     for dados2 in dadosSQLite:
#         if(str(dados[3]) == str(dados2[1])): #Verifica se o CPF já está no banco SQLite
#             encontrou = True
#             if(str(dados[0]) != str(dados2[0])): #Verifica se a data de registro no banco SQL Server é diferente da data de registro no banco SQLite
#                 try:
#                     print("Atualizando dados do colaborador " + str(dados[3]))
#                     cursor.execute("UPDATE dadosWelcome SET dt_server = ?, ticket = ?, nome = ?, empresa = ?, local_trabalho = ?, dt_welcome = ? WHERE cpf = ?", (dados[0], dados[1], dados[2], dados[4], dados[5], dados[6], dados[3]))
#                     connection.commit()
#                     print("Dados atualizados")
#                 except Exception as e:
#                     print("Erro ao atualizar dados")
#                     print(e)
#             break
#         else:
#             encontrou = False

#     if(encontrou == False): #Se o CPF não estiver no banco SQLite, insere os dados
#         try:
#             cursor.execute("INSERT INTO dadosWelcome VALUES (?,?,?,?,?,?,?)", dados)
#             print("Novo colaborador: " + str(dados[3]))
#             n+=1
#             print(n)
#             connection.commit()
#         except Exception as e:
#             print("Erro ao inserir colaborador: " + str(dados[3]))
#             print(e)


# #Verificando se há colaboradores que foram cancelados
# horaAtual = datetime.now()
# listaLG = []
# for dados in dadosLGSQLite:
#     listaLG.append(dados[0])
# n = 1
# for dados in dadosSQLite:
#     dataWelcome = datetime.strptime(dados[2], '%Y-%m-%d')
#     if dados[1] not in listaLG and horaAtual > dataWelcome: #verifica se cpf da base SQLite nao esta na base lg e se a data do welcome ja passou
#         print('deletando colaborador fora da base lg: ' + str(dados))
#         print(n)
#         try:
#             cursor.execute("DELETE FROM dadosWelcome WHERE cpf = '{}'".format(dados[1]))
#             connection.commit()
#             print("Dados removidos")
#         except Exception as e:
#             print("Erro ao remover  dados")
#             print(e)
#         n+= 1

# connection.close()
# querySQL.finalizaConexao()        