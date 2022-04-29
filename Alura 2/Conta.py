#from Conta import CONTA
'''Uma classe é uma especificação de um tipo, definindo valores e comportamentos.
Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos.
Uma boa analogia é considerar a classe como a receita para a criação de algum prato.'''
class CONTA:
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

conta = CONTA(123, "Igor", 10, 100) 

#funcao extrato esta dentro da classe CONTA. conta.extrato usa a variavel tuple conta como referencia
conta.extrato()

conta.deposita(100)

conta.saca(50)