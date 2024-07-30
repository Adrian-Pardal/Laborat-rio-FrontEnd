from flask import Flask , render_template
from informacao import Informacao
from eventos import Eventos
from organizacao import Organizacao
from cantina import Cantina
from comida import Comida
from seguranca import Seguranca
from transporte import Transporte
from bloco import Bloco

app = Flask(__name__)

informacao1 = Informacao('img/TelaHome/Eventos.jpg' , 'Eventos' , 'Todos Eventos Que Acontece Na Faculdade' , 'Eventos')
informacao2 = Informacao('img/TelaHome/Campus.jpg' , 'Campus' , 'Tudo Sobre o Campus' , 'Campus')
informacao3 = Informacao('img/TelaHome/ClubeEorganizacao.jpg' , 'Clube e Organização' , 'Os clubes e Organizações do Campus' , 'organizacao')
informacao4 = Informacao('img/TelaHome/Servicao.jpg' , 'Serviços' , 'Serviços Prestados na Universidade' , 'servico')
informacao5 = Informacao('img/TelaHome/transporte.jpg' , 'Transporte' , 'Transporte Fornecidos da Faculdade' , 'transporte' )

informacao_all = [informacao1 , informacao2 , informacao3 , informacao4 , informacao5]

@app.route('/')
def home():
    return render_template('home.html' , informacao = informacao_all)

evento1 = Eventos(1 , "img/TelaEventos/palestra.png" , "palestra", "Vida de Programar" , "09/06/2024", "bloco 9", "lucas" ," https://forms.gle/U68cUZicBeUHeKK26" , "18:20")
evento2 = Eventos(2 , "img/TelaEventos/laboratorio.png", "laboratorio" , "Laboratoria Java" , "29/05/2024","bloco 8" , "roni" , "https://forms.gle/U68cUZicBeUHeKK26", "14:30")

evento3 = Eventos(3 , "img/TelaEventos/palestra.png" , "palestra", "Technologias e Mudanças" , "17/05/2024", "bloco 9", "lucas" ," https://forms.gle/U68cUZicBeUHeKK26" ,"15:30")
evento4 = Eventos(4 , "img/TelaEventos/laboratorio.png", "laboratorio" , "Laboratoria Python" , "27/07/2024","bloco 8" , "roni" , "https://forms.gle/U68cUZicBeUHeKK26" ,"19:00")
eventos_all = [evento1 , evento2 , evento3 , evento4]


@app.route('/Eventos')
def Eventos():
    return render_template('TelaEventos.html' , eventos_list = eventos_all)

bloco1 = Bloco(1 , "Bloco 1" , "1° Piso ","2° Piso "," " ,"","• Biblioteca" ,"" ,"" ,"• Area de Reunião" ,"" ," ","" ,"" ,"setor6Piso2" ,"","")
bloco2 = Bloco(2 , "Bloco 2" , "1° Piso ","2° Piso " ," " ,"","• Pro-Reitoria de Extensão Universitária e Deportos" ,"" ,"" ,"• Salas de Aula" ,"" ," ","" ,"" ,"setor6Piso2" ,"" ,"")
bloco3 = Bloco(3 , "Bloco 3" , "1° Piso ","2° Piso " , "" ,"","• Secretaria Acadêmica de Graduação" ,"" ,"" ,"• Pró-Reitoria de Pesquisa e Pós-Gradução" ,"• Sala de Professores TI e Parcial" ," ","" ,"" ,"setor6Piso2","" ,"")

bloco4 = Bloco(4 , "Bloco 4" , "1° Piso ","2° Piso " ," " ,"","• Laborario de Medicina e Medicina Veterinaria" ,"" ,"" ,"• Salas de Aula" ,"" ," ","" ,"" ,"setor6Piso2","","")
bloco5 = Bloco(5 , "Bloco 5" , "1° Piso ","2° Piso " ," " ,"","• NApp - Nucleo de Apoio Psicopedagógico" ,"" ,"" ,"• Salas de Aula" ,"" ," ","" ,"" ,"setor6Piso2","","")
bloco6 = Bloco(6 , "Bloco 6" , "1° Piso ","2° Piso "," " ,"" ,"• Coordenação de Infraestrutura" ,"• Crea-RJ " ,"" ,"• Salas de Aula" ,"" ," ","" ,"" ,"setor6Piso2","","")

bloco7 = Bloco(7 , "Bloco 7" , "1° Piso ","2° Piso " ," " ," ","• Laboratorio de Quimíca" ,"• Laboratorio BioDiesel e Cevejaria" ,"" ,"• Estudio" ,"• Salas de Aula" ," ","" ,"" ,"","","")
bloco8 = Bloco(8 , "Bloco 8" , "1° Piso ","2° Piso " ,"3° Piso " ,"4° Piso ","• CPA - Comissão Propria de Avaliação" ,"• CED - Coordenação de Ensino Digital" ,"" ,"• Secretaria de Coordenação de Cursos" ,"• Vassouras Tech" ,"• Reitoria e Pró-Reitoria ","• Sala de Docentes" ,"• Sala NDE" ,"setor6Piso2" ,"• Salas de Aula","• Salas de Aula")
bloco9 = Bloco(9 , "Bloco 9" , "1° Piso ","2° Piso " ," " ," ","• Centra de Carreiras , Oportunidades de Estagios" ,"• Graduação Digital" ,"• Laboratorio de Eletrica e Civil" ,"• Laboratorio de Informatica" ,"• Auditorio" ," ","" ,"" ,"","","")
blocos = [bloco1 , bloco2 , bloco3, bloco4 , bloco5 , bloco6 , bloco7 , bloco8 , bloco9]


@app.route('/Campus')
def Campus():
    return render_template('TelaCampus.html' , blocos = blocos)


clube1 = Organizacao(1 ,"img/TelaClubeOrgonizacao/atleticaEngenharia.jpg" , "Atletica de Engenharia" , "Cursos Engenharias" , "Associação Atletica de Engenharia", "https://www.instagram.com/atleticaengvassouras/")
clube2 = Organizacao(2 ,"img/TelaClubeOrgonizacao/atleticaxama.jpg" , "Atletica de Enfermagem" , "Curso Enfermagem" , "Associação Atletica de Enfermagem", "https://www.instagram.com/atleticaengvassouras")

clube_all = [clube1 , clube2]

@app.route('/Organizações')
def organizacao():
    return render_template('TelaClubeOrganizacao.html' , clube_list = clube_all)


cantina1 = Cantina(1 ,"Cantina Universiratária" , "Atras Do Bloco 2 ","Das 8:00 as 11:00", "Das 18:30 as 21:30" , "Diurno e Noturno" , "Cantina")
cantina = [cantina1]

comida1 = Comida(1 , "coxinha" , "img/TelaServico/img/coxinha.jpg" ,"8,00")
comida2 = Comida(2 , "joelho" , "img/TelaServico/img/joelho.jpg" ,"9,50")
comida3 = Comida(3 , "coca lata" , "img/TelaServico/img/cocalata.jpg" ,"6,00")
comida4 = Comida(4 , "guarana lata" , "img/TelaServico/img/guaranalata.jpg" ,"6,00")

comida_all = [comida1 , comida2 , comida3 , comida4]

seguranca1 = Seguranca( 1 , "Segurança e Vigía", "24h" , "Diurno", "Noturno" , "Todas as entradas temos Vigias" , "img/TelaServico/img/Segurança.jpg")
seguranca = [seguranca1]

@app.route('/Serviços')
def servico():

    return render_template('TeladeServiçosnoCampus.html', cantina = cantina, comida = comida_all , seguranca = seguranca)

transporte1 = Transporte( 1 , "Onibus" , "Paty do Alferes" , "Na frente do Bramil" , "22:10" , "Segunda a Sexta" ,"Onibus", "img/TelaTransporte/onibus.jpg", "https://www.whatsapp.com/?lang=pt_BR")
transporte2 = Transporte( 2 , "Van" , "Volta Redonda" , "na rua de cima da faculdade" , "22:10" , "Segunda a Sexta" ,"Van", "img/TelaTransporte/van.jpg","https://www.whatsapp.com/?lang=pt_BR")
transporte3 = Transporte( 3, "Onibus" , "Mendes" , "Rodo da Fundação" , "22:30" , "Segunda a Sexta" ,"Onibus", "img/TelaTransporte/onibus.jpg" ,"https://www.whatsapp.com/?lang=pt_BR")
transporte4 = Transporte( 4 , "Van" , "Pirai" , "Na frente do Bramil" , "22:30" , "Segunda a Sexta" ,"Van", "img/TelaTransporte/van.jpg", "https://www.whatsapp.com/?lang=pt_BR")
transporte5 = Transporte( 5 , "Van" , "Barra do Pirai" , "Rdoviaria Velha" , "22:30" , "Segunda a Sexta" ,"Van", "img/TelaTransporte/van.jpg" ,"https://www.whatsapp.com/?lang=pt_BR")
transporte6 = Transporte( 6, "Onibus" , "Valença" , "Rodo da Fundação" , "22:30" , "Segunda a Sexta" ,"Onibus", "img/TelaTransporte/onibus.jpg" , "https://www.whatsapp.com/?lang=pt_BR")
transporte7 = Transporte( 7, "Onibus" , "Miguel Pereira" , "Rodo da Fundação" , "22:30" , "Segunda a Sexta" ,"Onibus", "img/TelaTransporte/onibus.jpg" , "https://www.whatsapp.com/?lang=pt_BR")
transporte8 = Transporte( 5 , "Van" , "Três Rios" , "Rodoviaria Velha" , "22:30" , "Segunda a Sexta" ,"Van", "img/TelaTransporte/van.jpg" ,"https://www.whatsapp.com/?lang=pt_BR")

transporte_all = [transporte1 , transporte2 , transporte3 , transporte4 , transporte5 , transporte6 , transporte7 , transporte8]

@app.route('/Transporte')
def transporte():
    return render_template('TeladeTransporteeAcesso.html', transporte_list = transporte_all	)

if __name__ in "__main__":
    app.run(debug=True)