"""puppet.py: modulo principal do puppet"""
#import logging
from flask import Flask, Blueprint, render_template
from endpoints.temperature import ns as access_event_endpoint
from endpoints.main_page import ns as page_endpoint
from configure import api


app = Flask(__name__)


def configure_app():
    """modulo de configuracao do objeto puppet"""
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def initialize_app():
    """modulo de inicializacao do puppet"""
    configure_app()
    blueprint = Blueprint('api', __name__, url_prefix='')
    # quando rodamos na maquina local, a inicializacao do server eh aqui.
    api.init_app(blueprint)
    api.add_namespace(access_event_endpoint)
    api.add_namespace(page_endpoint)
    app.register_blueprint(blueprint)


@app.route("/")
def index():
    return render_template('static/index.html')


def main():
    """modulo principal o qual o puppet eh inicializado"""
    initialize_app()
    # logging.basicConfig(filename='LogsDebugPuppet.log',
    #                    filemode='a',
    #                   format='%(asctime)s %(name)s %(levelname)s:%(message)s',
    #                  datefmt='%m/%d/%Y %I:%M:%S %p',
    #                 level=logging.INFO, force=True)"""
    app.run(debug=True, port=8080)

# @app.before_first_request
# def cria_banco():
   # banco.create_all()


if __name__ == '__main__':
    main()
#   banco.init_app(app)#quando rodamos na maquina local, a inicializacao do server eh aqui.
    #app.run(debug = True, port = 80)
