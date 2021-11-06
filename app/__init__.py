from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rating.db'

    db = SQLAlchemy(app)

    class Rating(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        star = db.Column(db.Integer)
        evaluation = db.Column(db.String(500))
        date_created = db.Column(db.DateTime, default=datetime.utcnow)

        def __repr__(self):
            return '<ID %r>' %self.id

    @app.route('/')
    def index():
        evaluations = Rating.query.order_by(Rating.date_created)
        return render_template('index.html', evaluations=evaluations)

    @app.route('/contato')
    def contato():
        return render_template('contato.html')
        

    @app.route('/rating', methods=["POST", "GET"])
    def rating():
        if request.method == "POST":                
            star_rating = request.form.get("rating")
            comment = request.form.get("comment")
            new_rating = Rating(star = star_rating, evaluation = comment )
        
            try:
                db.session.add(new_rating)
                db.session.commit()

                return redirect('/')
            except:
                return "Erro ao adicionar ao banco de dados"
        else:
            return redirect('/')

    return app
# Retire o comentario para testar via Pycharm
test = create_app()
test.run()