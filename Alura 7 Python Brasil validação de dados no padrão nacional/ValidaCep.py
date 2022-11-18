import sys

class BuscaEndereco:

    def __init__(self, cep):
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



if(__name__ == "__main__"):
    novoCep = BuscaEndereco('12345678')
    novoCep.formataCep()