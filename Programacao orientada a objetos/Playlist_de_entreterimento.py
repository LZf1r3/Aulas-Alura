class Programa:
    def __init__(self, nome, ano):
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
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} -{self.temporadas} temporadas - {self.likes} Likes'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


atlanta = Serie("Atlanta", 2018, 2)
vingadores = Filme("Vingadores - guerra infinita", 2018, 160)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

atlanta.adicionar_like()
atlanta.adicionar_like()
vingadores.adicionar_like()
tmep.adicionar_like()
tmep.adicionar_like()
tmep.adicionar_like()
tmep.adicionar_like()
demolidor.adicionar_like()

filmes_e_series = [atlanta, demolidor, vingadores, tmep]
playlist_fim_de_semana = Playlist("playlist_fim_de_semana", filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)
