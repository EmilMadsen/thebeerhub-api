from flask import request
from flask_restplus import Resource

from app.main.model.dto import BrewDto
from ..service.brew_service import save_brew, get_all_brews, get_a_brew, delete_a_brew
from ..service import tilt_service

api = BrewDto.api
_brew = BrewDto.brew


@api.route('/')
class BrewList(Resource):
    @api.doc('list_of_brews')
    @api.marshal_list_with(_brew, envelope='data')
    def get(self):
        return get_all_brews()

    @api.response(201, 'brew successfully created.')
    @api.doc('create or update brew')
    @api.expect(_brew, validate=True)
    @api.marshal_with(_brew)
    def post(self):
        print(request.json)
        data = request.json
        return save_brew(data=data)


@api.route('/<id>')
@api.param('id', 'The brew id')
@api.response(404, 'Brew not found.')
class Brew(Resource):
    @api.doc('get a brew')
    @api.marshal_with(_brew)
    def get(self, id):
        """get a brew given its identifier"""
        brew = get_a_brew(id)
        if not brew:
            api.abort(404)
        else:
            return brew

    @api.doc('delete a brew')
    def delete(self, id):
        return delete_a_brew(id)


@api.route('/job/tilt')
class FetchJob(Resource):
    def get(self):
        tilt_service.fetch_tilt_data("https://docs.google.com/spreadsheets/d/1XWo5ZkoweSnvKIlnR0X1tuKgKaq7UcQgQrDI0cA_KpQ/export?format=csv&gid=0")


