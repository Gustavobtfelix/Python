import requests
import sys


class BuscaCep:

    def __init__(self, cep, colaborador=None):
        cep = str (cep)
        self.validaCep(cep)
            

    def validaCep(self, cep):
        try:
            if len(cep) == 8:
                self.cep = cep
            else:
                raise ValueError ("Quantidade de caracteres invalida")
        except Exception as e:
            print (e)
            sys.exit(1)

    def formataCep(self):
        print("{}-{}".format(self.cep[:4], self.cep[4:]))

    def acessaApiCep(self):
        
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        value = requests.get(url, verify=False)
        print(value.text)
        dados = value.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )


if(__name__ == "__main__"):
    novoCep = BuscaCep('01001000')
    bairro, cidade, uf = novoCep.acessaApiCep()
    print(bairro, cidade, uf)