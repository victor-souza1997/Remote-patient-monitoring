#!/usr/bin/env python

"""config_puppet.py: Arquivo inicializa objeto api"""


from flask_restx import Api

api = Api(
    version="0.2",
    title="API_Ciclope_Puppets",
    description="Api responsável por interfacear dispositivos de controle de acesso.",
    terms_url="/",
    contact="leones.santos@bktele.com.br",
    # license="",
    license_url="192.168.10.81:5020",
    # endpoint="",
    default="Ciclope",
    default_label="olho vivo",
    default_mediatype="Ciclope",
    validate=True,
    ordered=True,
    doc="/doc",
    # decorators=[],
    # authorizations=[],
    # serve_challenge_on_401=True,
    # format_checker,
    # url_scheme,
    default_swagger_filename="Swagger_filename")
