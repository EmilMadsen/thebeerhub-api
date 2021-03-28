from flask import request
from flask_restplus import Resource

from app.main.model.dto import BrewDto
from ..service.brew_service import save_brew, get_all_brews, get_a_brew

api = BrewDto.api
_brew = BrewDto.brew


@api.route('/')
class BrewList(Resource):
    @api.doc('list_of_brews')
    @api.marshal_list_with(_brew, envelope='data')
    def get(self):
        """List all brews"""
        return get_all_brews()

    @api.response(201, 'brew successfully created.')
    @api.doc('create or update brew')
    @api.expect(_brew, validate=True)
    def post(self):
        """Creates a new Brew """
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
