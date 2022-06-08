class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self): #__str__ altera o comando print referente a funcao
        return(f'Nome: {self.nome} Ano {self.ano} Likes: {self.likes}')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return(f'Nome: {self.nome} Ano {self.ano} Duracao {self.duracao} Likes: {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self): #def imprime
        return(f'Nome: {self.nome} Ano {self.ano} temporadas {self.temporadas} Likes: {self.likes}')

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)    

'''
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
'''


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

"""
print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')
"""
lista = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', lista)

for programa in minha_playlist:
    #print(f'Nome: {programa.nome} - Likes: {programa.likes}')
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')
