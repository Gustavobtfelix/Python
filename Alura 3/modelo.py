class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

avengers = Filme('vingadores', 2016, 160)
print(f'Nome: {avengers.nome} - Ano: {avengers.ano}'
      f' - Temporadas: {avengers.duracao}')

atlanta = Serie('atlanta', 2018, 3)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f' - Temporadas: {atlanta.temporadas}')