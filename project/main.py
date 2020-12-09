#перед запуском необходимо выполнить 'pip install flask, flask_sqlalchemy, flask_login' в терминале 

#игры хранятся на ресурсе https://trinket.io/
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/poker')
def poker():
    return render_template('poker.html')

@app.route('/roulette')
def roulette():
    return render_template('roulette.html')

if __name__=="__main__":                             
    app.run(debug=True)     
