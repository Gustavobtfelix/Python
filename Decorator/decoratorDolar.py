import requests
import time

# criar um decorator calcular_tempo
def calcular_tempo(funcao):
    def wrapper():
        try:
            print("Vou pegar a cotacao")
            oi = funcao()
            print("Terminei de pegar a cotacao")
            return oi
        except Exception as e:
            print("Erro ao pegar a cotacao")
    return wrapper

@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])
    return 'oi'


oi = pegar_cotacao_dolar()

print(oi)