from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        # return render_template('index.html')

        return render_template('index.html')

    @app.route('/rating', methods=["POST"])
    def rating():
        star_rating = request.form.get("rating");
        comment = request.form.get("comment")
        return render_template('index.html', star_rating=star_rating, comment=comment)

    return app

# Retire o comentario para testar via Pycharm
test = create_app()
test.run()