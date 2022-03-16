from flask import render_template
from flask_restx import Resource
from configure import api

ns = api.namespace('', description='Operations related to blog posts')


@ns.route('/page')
class MainPage(Resource):
    def get(self):
        return render_template('index.html')
