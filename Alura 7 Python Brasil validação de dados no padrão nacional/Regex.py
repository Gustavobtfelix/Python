import re

# padrao = "[0-9][a-z]{2}[0-9]" #numero, letra e quantidade, numero
# texto = "123 1ab2 1cc aa1"
# resposta = re.search (padrao, texto) #busca
# print (resposta.group())

padrao = "\w{5,50}@[a-z]{3,10}.com(.br)?"
texto = "aaabbbcc rodrigo123@gmail.com.br uyfbsufbsfbbff"
resposta = re.search(padrao, texto)
print (resposta.group())
