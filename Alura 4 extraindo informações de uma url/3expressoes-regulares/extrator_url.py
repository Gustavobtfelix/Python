import re  #Regular Expression -- RegEx
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.replace(" ", "")
        else:
            return ""

    def valida_url(self):
        if not self.url: # se bool(url) for false
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')    #(qualquer caracter) [exatos caracter]
        match = padrao_url.match(self.url)    
        if not match:
            raise ValueError("A URL nao e valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        parametro_busca = parametro_busca
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor: indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)
    def __str__(self):
        return "Essa classe possui\n URL: " + self.url + "\n Parâmetros: " + self.get_url_parametros() + "\n URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"

extrator_url = ExtratorURL(url)
print("Tamanho da URL:", len(extrator_url))
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(extrator_url)

extrator_url2 = ExtratorURL(url)
print(extrator_url == extrator_url2) # == compara valor pelo metodo __eq__, is compara posicao em memoria dos objetos
print(id(extrator_url)) #id mostra alocacao em memoria
print(id(extrator_url2))
#verifica a classe de qualquer objeto utilizando o "type(nomeDoObjeto)"
#type(None)