from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        # return render_template('index.html')

        return render_template('testeBootstrp2.html')
    return app

'''Retire o comentario para testar via Pycharm'''
# test = create_app()
# test.run()