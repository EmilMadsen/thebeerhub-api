from flask import request
from flask_restplus import Resource

from..service import step_service
from app.main.model.dto import BrewStepDto

api = BrewStepDto.api
_step = BrewStepDto.step


@api.route('/parent/<parent_id>')
@api.param('parent_id', 'The parent brew id')
class StepList(Resource):
    @api.doc('list_of_brew_steps')
    @api.marshal_list_with(_step, envelope='data')
    def get(self, parent_id):
        return step_service.get_steps_by_parent_id(parent_id)


@api.route('/parent/<parent_id>/active')
@api.param('parent_id', 'The parent brew id')
class Step(Resource):
    @api.doc('current active step')
    @api.marshal_with(_step)
    def get(self, parent_id):
        return step_service.get_current_active_step(parent_id)


@api.route('/parent/<parent_id>/next/<timestamp>')
@api.param('parent_id', 'The parent brew id')
@api.param('timestamp', 'The timestamp that the step should start/stop at')
class Step(Resource):
    @api.doc('end current active and go to next step')
    @api.marshal_with(_step)
    def post(self, parent_id, timestamp):
        return step_service.go_to_next_step(parent_id, timestamp)


@api.route('/')
class Step(Resource):
    @api.response(200, 'step successfully updated.')
    @api.doc('update brew step')
    @api.expect(_step)
    @api.marshal_with(_step)
    def post(self):
        data = request.json
        return step_service.update_step(data=data)
