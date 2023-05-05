class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self_nome = novo_nome.title()
    
    def adicionar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
    
    def tamanho(self):
        return len(self.programas)
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self.nome} - {self.ano} -{self.temporadas} temporadas - {self.likes} Likes'

atlanta = Serie("Atlanta", 2018, 2)
vingadores = Filme("Vingadores - guerra infinita", 2018, 160)


atlanta.adicionar_like()
atlanta.adicionar_like()
vingadores.adicionar_like()


filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    print(programa)
