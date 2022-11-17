from validate_docbr import CPF, CNPJ
import sys

class Documento:
    @staticmethod
    def criar_novo(documento):
        try:
            doc = str(documento)
            doc = doc.replace(".", "")
            doc = doc.replace("-", "")
            doc = doc.replace("/", "")
            doc = doc.strip()
            if len(doc) == 11:
                return ValidaDocumento(doc, 'cpf')
            elif len(doc) == 14:
                return ValidaDocumento(doc, 'cnpj')
            else:
                raise ValueError ("Quantidade de caracteres invalida! use 'cpf' or 'cnpj'")
        except Exception as e:
            print (e)
            sys.exit(1)

class ValidaDocumento:
    def __init__(self, documento, tipoDocumento):
        self.tipoDocumento = tipoDocumento
        if (tipoDocumento == 'cpf'):
            self.validaCPF(documento)
        elif (tipoDocumento == 'cnpj'):
            self.validaCNPJ(documento)

    def __str__(self): #é chamado quando alguem da print
        if self.tipoDocumento == 'cpf':
            return self.cpf
        if self.tipoDocumento == 'cnpj':
            return self.cnpj

    def validaCPF(self, cpf):
        try:
            validadorCpf = CPF()
            if (validadorCpf.validate(cpf)):
                self.cpf = validadorCpf.mask(cpf)
            else:
                raise ValueError ("cpf invalido")
        except Exception as e:
            print (e)
            sys.exit(1)

    def validaCNPJ(self, cnpj):
        try:
            validadorCNPJ = CNPJ()           
            if(validadorCNPJ.validate(cnpj)):
                self.cnpj = validadorCNPJ.mask(cnpj)
            else:
                raise ValueError ("cnpj invalido")
        except Exception as e:
            print (e)
            sys.exit(1)



if(__name__ == "__main__"):
    exemplocpf = 12818792746
    cpf = Documento.criar_novo(exemplocpf)
    print(cpf)

    exemplo_cnpj = 35379838000112
    cnpj = Documento.criar_novo(exemplo_cnpj)
    print(cnpj)
