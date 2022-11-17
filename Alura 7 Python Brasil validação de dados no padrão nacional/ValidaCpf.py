from validate_docbr import CPF
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        documento = documento.replace(".", "")
        documento = documento.replace("-", "")
        documento = documento.strip()
        documento = documento.zfill(11)
        if self.validaCPF(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def validaCPF(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida!")

    def formataCPF(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self): #é chamado quando alguem da print
        return self.formataCPF()



if(__name__ == "__main__"):
    cpf = 12345678911
    objetoCpf = Cpf(cpf)
    print(objetoCpf)
