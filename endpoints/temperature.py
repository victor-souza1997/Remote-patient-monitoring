from flask import request
from flask_restx import Resource, reqparse
from configure import api
from dateutil.parser import parse
from functions import get_temperature_db, load_array_points
ns = api.namespace('', description='Operations related to blog posts')


@ns.route('/temperature')
class Hikivison(Resource):
    def post(self):
        root_parser = reqparse.RequestParser()
        root_parser.add_argument('sensor', type=dict)
        root_args = root_parser.parse_args()
        event_parser = reqparse.RequestParser()
        event_parser.add_argument(
            'temperature', type=float, location=('sensor'))
        print(root_args)
        return 500

    def get(self):
        return get_temperature_db()


@ns.route('/temperature/array')
class TemperatureToArray(Resource):
    def get(self):

        return load_array_points()
