from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///rating.db'

db = SQLAlchemy(app)

class rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer)
    evaluation = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<ID %r>' %self.id

@app.route('/')
def index():
    # return render_template('index.html')

    return render_template('index.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/rating', methods=["POST"])
def rating():
    star_rating = request.form.get("rating");
    comment = request.form.get("comment")
    return render_template('index.html', star_rating=star_rating, comment=comment)


# Retire o comentario para testar via Pycharm
# test = create_app()
# test.run()