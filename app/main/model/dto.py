from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class BrewDto:
    api = Namespace('brew', description='brew related operations')
    brew = api.model('brew', {
        'brew_name': fields.String(required=True, description='brew name'),
        'brew_type': fields.String(required=True, description='brew type')
    })