from flask import request
from flask_restplus import Resource

from app.main.model.dto import BrewStepDto
from ..service.step_service import get_steps_by_parent_id, update_step

api = BrewStepDto.api
_step = BrewStepDto.step


@api.route('/parent/<parent_id>')
@api.param('parent_id', 'The parent brew id')
class StepList(Resource):
    @api.doc('list_of_brew_steps')
    @api.marshal_list_with(_step, envelope='data')
    def get(self, parent_id):
        return get_steps_by_parent_id(parent_id)


@api.route('/')
class Step(Resource):
    @api.response(200, 'step successfully updated.')
    @api.doc('update brew step')
    @api.expect(_step)
    def post(self):
        data = request.json
        return update_step(data=data)
