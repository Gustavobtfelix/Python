#from Conta import CONTA
'''Uma classe é uma especificação de um tipo, definindo valores e comportamentos.
Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos.
Uma boa analogia é considerar a classe como a receita para a criação de algum prato.'''
class CONTA:
    #pass           /Usado quando a classe é vazia
    #funcao construtora. _init_ salva a funcao na memoria para usar depois. (self) = referencia
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        #adiciona atributos ao self. #!os parametros do teste.py
        #Atributos com __ sao privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #metodo para pegar valor privado
   # def get_limite(self):
    @property
    def limite(self):
        return self.__limite
    #metodo para alterar valor privado
    #def set_saldo(self, saldo):
    @limite.setter       #precisa ser declarado a property antes
    def limite(self, limite):
        self.__limite = limite

conta = CONTA(123, "Marco", 10, 100) 
conta2 = CONTA(321, "Polo", 100, 500)

#funcao extrato esta dentro da classe CONTA. conta.extrato usa a variavel tuple conta como referencia
conta.extrato()

conta.deposita(100)

conta.saca(50)

conta2.transfere(45, conta)

conta.limite

conta.limite = 200
