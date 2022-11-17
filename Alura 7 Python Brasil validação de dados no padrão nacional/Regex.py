import re

# padrao = "[0-9][a-z]{2}[0-9]" #numero, letra e quantidade, numero
# texto = "123 1ab2 1cc aa1"
# resposta = re.search (padrao, texto) #busca
# print (resposta.group())

# #padrao email br
# padrao = "\w{5,50}@[a-z]{3,10}.com(.br)?" #valor entre 5 e 50 digitos, @, letra entre 3 e 10, .com e .br opcional
# texto = "aaabbbcc rodrigo123@gmail.com.br uyfbsufbsfbbff"
# resposta = re.search(padrao, texto)
# print (resposta.group())


#padrao telefone fixo e celular
#padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
padrao = "[(]?[0-9]{2}[)]?[0-9]{4,5}[-]?[0-9]{4}"
texto = "eu gosto do numero 2126451234 e gosto também do (21)93643-1234"
resposta = re.findall(padrao, texto)

print(resposta)
