from validate_docbr import CPF, CNPJ
import sys
class CPFCNPJ:
    def __init__(self, documento, tipoDocumento):
        self.tipoDocumento = tipoDocumento
        if (tipoDocumento == 'cpf'):
            self.validaCPF(documento)
        elif (tipoDocumento == 'cnpj'):
            self.validaCNPJ(documento)
        else:
             raise ValueError ("Tipo não existe! use 'cpf' or 'cnpj'")



    def __str__(self): #é chamado quando alguem da print
        if self.tipoDocumento == 'cpf':
            return self.cpf
        if self.tipoDocumento == 'cnpj':
            return self.cnpj

    def validaCPF(self, doc):
        try:
            cpf = str(doc)
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            cpf = cpf.strip()
            cpf = cpf.zfill(11)
            if(len(cpf) != 11):
                raise ValueError ("Quantidade de digitos inválida!!")
                
            validadorCpf = CPF()
            if (validadorCpf.validate(cpf)):
                self.cpf = validadorCpf.mask(cpf)
            else:
                raise ValueError ("cnpj invalido")
        except Exception as e:
            print (e)
            sys.exit(1)

    def validaCNPJ(self, doc):
        try:
            cnpj = str(doc)
            cnpj = cnpj.replace(".", "")
            cnpj = cnpj.replace("/", "")
            cnpj = cnpj.replace("-", "")
            cnpj = cnpj.strip()
            cnpj = cnpj.zfill(14)
            if len(cnpj)!= 14:
                raise ValueError ("Quantidade de digitos inválida!!")

            validadorCNPJ = CNPJ()           
            if(validadorCNPJ.validate(cnpj)):
                self.cnpj = validadorCNPJ.mask(cnpj)
            else:
                raise ValueError ("cnpj invalido")
        except Exception as e:
            print (e)
            sys.exit(1)





    



if(__name__ == "__main__"):
    cpf = 12818792746
    objetoCpf = CPFCNPJ(cpf, 'cpf')
    print(objetoCpf)

    # exemplo_cnpj = "3537983800011"
    # cnpj = CNPJ()
    # print(cnpj.validate(exemplo_cnpj))


    exemplo_cnpj = 35379838000112
    cnpj = CPFCNPJ(exemplo_cnpj, 'cnpj')
    print(cnpj)
