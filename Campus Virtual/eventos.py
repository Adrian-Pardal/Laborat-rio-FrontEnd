
#Objetivo: Listar eventos acadêmicos, como palestras, workshops e seminários.
#Funcionalidades: Visualização de eventos, detalhes sobre datas, locais, palestrantes, e a possibilidade de inscrição nos eventos.


class Eventos:
    def __init__(self ,id , foto ,  categoria , nome , data , local , palestrante, page_url , hora):
        self.id = id
        self.foto = foto
        self.categoria = categoria
        self.nome = nome
        self.data = data
        self.local = local
        self.palestrante = palestrante
        self.page_url = page_url
        self.hora = hora