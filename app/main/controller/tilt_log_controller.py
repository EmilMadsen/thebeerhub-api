from flask_restplus import Resource
from ..service import tilt_service
from app.main.model.dto import TiltLogDto

api = TiltLogDto.api
_tilt_log = TiltLogDto.tilt_log


@api.route('/parent/<parent_id>')
@api.param('parent_id', 'The parent brew id')
class StepList(Resource):
    @api.doc('list_of_tilt_logs')
    @api.marshal_list_with(_tilt_log, envelope='data')
    def get(self, parent_id):
        return tilt_service.get_tilt_logs_by_brew_id(parent_id)


@api.route('/start/jobs')
class FetchJob(Resource):
    def post(self):
        tilt_service.update_all_tilt_data()

