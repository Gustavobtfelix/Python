#url = "hrrps://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
#              dominio,    área(query/parametro) &(separa parametros)

#Sanitizacao da URL
url = url.replace(" ", "")

#url.strip()   remove todos os espacos em branco do inicio e do fim e caracteres especiais
#url.lstrip()
#url.rstrip()

#validacao da URL
if url == "":
    raise ValueError("A URL está vazia")

print(url)
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#busca somente nos parametros
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor: indice_e_comercial]
print(valor)