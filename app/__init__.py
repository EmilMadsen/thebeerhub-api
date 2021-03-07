# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.brew_controller import api as brew_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='The Beer Club - Beerhub',
          version='1.0',
          description='brew api for all kinds of data'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(brew_ns, path='/brew')
