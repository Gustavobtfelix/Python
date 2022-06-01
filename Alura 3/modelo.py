class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

avengers = Filme('vingadores', 2016, 160)
print(f'Nome: {avengers.nome} - Ano: {avengers.ano}'
      f' - duracao: {avengers.duracao} min - Likes: {avengers.likes}')

atlanta = Serie('atlanta', 2018, 3)
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f' - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')