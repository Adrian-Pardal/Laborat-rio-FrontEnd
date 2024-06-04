#
#python -m pip install --upgrade pip
#
#python -m pip install flask
#
#https://code.visualstudio.com/docs/python/tutorial-flask
#

from flask import Flask , render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOBER'

@app.route('/')
def home():

    return  render_template('home.html')

@app.route('/LadingPage')
def landingpage():

    return render_template('landingpage.html')

@app.route('/mario')
def mario():

    return render_template('mario.html')

@app.route('/racionais')
def racionais():

    return render_template('racionaismcs.html')












if __name__ in "__main__":
    app.run(debug=True)
