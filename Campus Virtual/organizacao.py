
#Objetivo: Apresentar os diferentes clubes e organizações estudantis, promovendo a interação comunitária.
#Funcionalidades: Descrições dos clubes, agenda de eventos, formulário de adesão e notícias recentes

class Organizacao:

    def __init__(self, id ,foto , nome , curso , descricao, page_url):
        self.id = id
        self.foto = foto
        self.nome = nome
        self.curso = curso
        self.descricao = descricao
        self.page_url = page_url

