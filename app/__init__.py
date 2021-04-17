# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.brew_controller import api as brew_ns
from .main.controller.step_controller import api as step_ns
from .main.controller.tilt_log_controller import api as tilt_log_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='The Beer Club - Beerhub',
          version='1.0',
          description='brew api for all kinds of data'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(brew_ns, path='/brew')
api.add_namespace(step_ns, path='/step')
api.add_namespace(tilt_log_ns, path='/tilt_logs')
