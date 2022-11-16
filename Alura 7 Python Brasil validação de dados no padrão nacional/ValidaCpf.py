class CPF:
    def __init__(self, documento):
        documento = str(documento)
        if self.validaCPF(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def validaCPF(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False



if(__name__ == "__main__"):
    cpf = 12345678911
    objetoCpf = CPF(cpf)
