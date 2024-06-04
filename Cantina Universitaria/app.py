from flask import Flask , render_template
from comida import Comida
from comentario import Comentario


app = Flask(__name__)

#_________________________________
Hambuguer = Comida(id= 1 ,img="img/hambuguer/hambuguer.jpg" ,banner="img/hambuguer/hambuguer-banner.jpg", nome="Hambuguer" , preco=  "11,50" , ingrediente="Rodelas de tomate ,Alface, Presunto,Queijo,Bacon,Hambúrguer,Ovo e Pão" , modoPreparo="Frite o bacon, o hambúrguer e o ovo . Após ter fritado o bacon, o hambúrguer e o ovo corte o pão e de uma leve torrada . Em seguida no pão coloque a alface, as rodelas de tomate e o bacon . Em uma frigideira coloque o hambúrguer, o ovo, duas fatias de presunto e duas fatias de queijo. Coloque uma tampa para abafar, retire quando o queijo estiver derretido e coloque no pão. Agora é só aproveitar.")
Coxinha = Comida(id= 2 ,img="img/coxinha/coxinha.jpg" ,banner="img/coxinha/coxinha-banner.jpg", nome="Coxinha" , preco=  "6,50" , ingrediente="Para a massa: 2 litros de água , farinha de trigo ,1 kg de farinha de trigo peneirada , caldo de galinha , 2 caldos de galinha , margarina , 1 colher de margarina , sal , 1 colher rasa de sal , colorau , 1 colher de colorífico Recheio: frango , 1 kg de peito de frango cozido e desfiado , cebola , 2 cebolas médias picadas , salsa , 1 xícara de salsinha picada , pimenta vermelha , pimenta vermelha picada a gosto , alho , 2 dentes de alho amassados , sal , sal a gosto , colorífico , colorífico a gosto , óleo , oleo ou azeite de oliva. Para empanar : clara de ovo , 2 claras , água , 1 litro de água , sal , 1 pitada de sal , farinha de trigo , 2 xícaras (chá) de farinha de trigo , farinha , 2 kg de farinha de pão " , modoPreparo="1 - Para a massa: Em uma panela, junte a água (de preferência a água que cozinhou o frango), os dois caldos de galinha, a margarina, o sal e o colorífico. , 2 - Deixe a mistura no fogo até ferver. , 3 - Após levantar fervura, junte a farinha peneirada e, com o auxílio de uma colher de pau, vá mexendo sem parar até que a massa desgrude da panela. , 4 - Retire a do fogo e coloque sobre uma superfície lisa e untada com margarina. , 5 - Deixe esfriar e vá sovando a massa constantemente para não criar casca. , 6 - Para o recheio: Em uma panela com óleo ou azeite, adicione o alho amassado, a pimenta vermelha picada e a cebola picada, frite tudo até dourar, junte o peito de frango cozido e desfiado e refogue por alguns minutos. Junte o sal e o colorífico. , 7 - Desligue o fogo e acrescente a salsinha picada, misture bem e deixe esfriar. , 8 - Para a montagem: Passe um pouco de manteiga nas mãos, pegue uma porção da massa (dependendo qual seja o tamanho desejado da coxinha), faça uma bolinha e com o auxílio do dedo indicador faça uma cavidade na massa. , 9 - Coloque uma porção do recheio e feche pinçando a boca da cavidade com a parte interna do polegar e do indicador. , 10 - Para empanar: Misture a água e as claras, bata com o auxílio de um garfo por alguns minutos, junte o sal a farinha de trigo e bata até que as bolinhas de farinha desapareçam. , 11 - Passe as coxinhas prontas por essa mistura, tire o excesso e passe pela farinha de trigo. , 12 - Após terminar de empanar as coxinhas, repita a operação. , 13 - Para fritar: Em um tacho ou panela funda, coloque óleo suficiente para cobrir a coxinha, deixe esquentar bem (190º a 200º C) e frite as coxinhas aos poucos para que o óleo não esfrie, o que pode fazer com que as coxinhas venham a rachar. , 14 - Espere dourar bem, escorra e aproveite.")
Pudim = Comida(id= 3,img="img/pudim/pudim.jpg" ,banner="img/pudim/pudim-banner.jpg", nome="Pudim de Leite" , preco=  "35,50" , ingrediente="1 xícara de chá de açúcar , 1/2 (meia) xícara de chá de água , 3 ovos ,1 lata de leite condensado (395g) , 1 1/2 xícara de chá de leite (375ml) , 1/2 colher de sopa de Maizena" , modoPreparo="1 - Disponha o açúcar e a água em uma fôrma de pudim grande (28 cm) e misture até o açúcar dissolver. 2 - Leve ao fogo baixo e deixe cozinhar, sem mexer, por 10 minutos, ou até o caramelo estar marrom. Retire do fogo e com o auxílio das costas de uma colher, espalhe o caramelo por toda a fôrma. Reserve. 3 - Preaqueça o forno em temperatura média (180° C). 4 - No copo do liquidificar, coloque o leite condensado, o leite, os ovos e o amido de milho MAIZENA . Bata até obter uma mistura homogênea. 5 - Transfira a mistura à fôrma de pudim já caramelizada e cubra-a com papel-alumínio. 6 - Coloque a fôrma de pudim dentro de uma assadeira e leve ao forno em banho-maria, por 1 hora, ou até que o pudim esteja assado. 7 - Retire do forno, tire a fôrma de pudim de dentro da assadeira e deixe esfriar. Leve à geladeira, por no mínimo 2 horas. 8 - Depois de frio, desenforme sobre um prato e sirva em seguida.")
catalogo_comida = [Hambuguer , Coxinha , Pudim]

#_________________________________

Amanda  = Comentario(img="img/pessoas/Amanda.jpg" ,nome="Amanda" , comentario="Adorei" , categoria="Hambuguer")
Nanda  = Comentario(img="img/pessoas/Nanda.jpeg" ,nome="Nanda" , comentario="Maravilhoso" , categoria="Pudim")
Davi = Comentario(nome="Davi" , img="img/pessoas/Davi.webp" ,comentario="Calma Calabresso" , categoria="Hambuguer")
vanessa = Comentario(nome="Vanesa Lopes" , img="img/pessoas/vanessa.webp" ,comentario="Achei desenteresante", categoria="Coxinha")
comentarios = [vanessa , Amanda ,Nanda , Davi]

@app.route('/')
def catalogo():
    return render_template('catalago-comida.html' , comidas = catalogo_comida)

@app.route('/Comida/<int:id>')
def comida(id:int):
    for comida_do_catalogo in catalogo_comida:
        if comida_do_catalogo.id == id:
            return render_template('comida.html' , comida = comida_do_catalogo , comentarios=comentarios)
    return "<h1> Erro Não existe essa Pagina</h1>"











app.run(debug=True)