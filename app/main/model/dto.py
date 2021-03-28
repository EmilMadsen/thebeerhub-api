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
        'id': fields.String(required=True, description='brew identifier'),
        'brew_name': fields.String(required=True, description='brew name'),
        'brew_type': fields.String(required=True, description='brew type'),
        'datetime': fields.DateTime(description='brew date'),
        'brewsters': fields.String(description='who brewed the brew'),
        'location': fields.String(description='where was it brewed'),
        'recipe': fields.String(description='link to recipe'),
        'target_start_gravity': fields.Integer(description='target start gravity'),
        'actual_start_gravity': fields.Integer(description='actual start gravity'),
        'target_end_gravity': fields.Integer(description='target end gravity'),
        'actual_end_gravity': fields.Integer(description='actual end gravity'),
    })
