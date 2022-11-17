import re

padrao = "[0-9][a-z]{2}[0-9]" #numero, letra e quantidade, numero
texto = "123 1ab2 1cc aa1"
resposta = re.search (padrao, texto) #busca
print (resposta.group())
