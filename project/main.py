# перед запуском необходимо выполнить 'pip install flask, flask_sqlalchemy, flask_login' в терминале 

# Если вдруг возникнет проблема с db, то ctrl+shift+p -> Python: Linter -> pylint, а затем обратно 
# игры хранятся на ресурсе https://trinket.io/

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '1405200120010514'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

# модель для отзывов
class Answer(db.Model): 
    # id проставляется автоматически за счет атрибута primary_key
    id = db.Column(db.Integer, primary_key=True) 
    # атрибут nullable не даст возможность пользователю оставить поле незаполненным
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Answer('{self.title}', '{self.date_posted}')"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    answers=Answer.query.order_by(Answer.date_posted).all()
    return render_template('admin.html', data=answers)

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

@app.route('/answer', methods=['POST','GET'])
def answer():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        answer = Answer(title=title,content=content)

        try:
            db.session.add(answer)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так((("
    else:
        return render_template('answer.html')

if __name__ == "__main__":                            
    app.run(debug=True)     
