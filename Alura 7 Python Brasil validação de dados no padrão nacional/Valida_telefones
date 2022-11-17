import re
import sys

class TelefonesBr:
    def __init__(self, telefone):
        self.validaTelefone(telefone)
        self.formataTelefone()

    def validaTelefone(self, telefone):
        try:
            padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao, telefone)
            if resposta:
                self.numero = resposta
            else:
                raise ValueError("Numero incorreto")
        except Exception as e:
            print (e)
            sys.exit(1)

    def formataTelefone(self):
        numero_formatado = "+{}({}){}-{}".format(
            self.numero.group(1),
            self.numero.group(2),
            self.numero.group(3),
            self.numero.group(4))
        print(numero_formatado)


if(__name__ == "__main__"):
    telefone = "552174377342"

    telefone_objeto = TelefonesBr(telefone)