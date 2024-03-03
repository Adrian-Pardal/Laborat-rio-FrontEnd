#
#python -m pip install --upgrade pip
#
#python -m pip install flask
#
#https://code.visualstudio.com/docs/python/tutorial-flask
#
from flask import Flask, render_template,redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOBER'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jogomario')
def JogoMario():
    

    return render_template('mario.html')


@app.route('/racionaismcs')
def racionaismcs():
    

    return render_template('racionaismcs.html')


@app.route('/landingpage')
def landingpage():
    

    return render_template('landingpage.html')

@app.route('/conversor')
def conversorTemperatura():
    

    return render_template('conversor.html')

@app.route('/calculadoraIMC')
def calculadoraIMC():
    

    return render_template('calculadoraIMC.html')

@app.route('/relogiodigital')
def RelogioDigital():
    

    return render_template('RelogioDigital.html')

if __name__ in "__main__":
   app.run(debug=True)






