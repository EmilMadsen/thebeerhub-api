from flask_restplus import Namespace, fields


class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'


class NullableInteger(fields.Integer):
    __schema_type__ = ['integer', 'null']
    __schema_example__ = 'nullable integer'


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

    brew_step = api.model('BrewStep', {
        'id': fields.String(attribute='id'),
        'parent_id': fields.String(attribute='parent_id'),
        'name': fields.String(required=True, attribute='name'),
        'index': fields.Integer(attribute='index'),
        'started': fields.DateTime(attribute='started'),
        'ended': fields.DateTime(attribute='ended'),
    })

    brew = api.model('brew', {
        'id': NullableInteger(description='brew identifier'),
        'brew_name': fields.String(required=True, description='brew name'),
        'brew_type': fields.String(required=True, description='brew type'),
        'created': fields.DateTime(description='brew date'),
        'brewsters': NullableString(description='who brewed the brew'),
        'location': NullableString(description='where was it brewed'),
        'recipe': NullableString(description='link to recipe'),
        'target_start_gravity': NullableInteger(description='target start gravity'),
        'actual_start_gravity': NullableInteger(description='actual start gravity'),
        'target_end_gravity': NullableInteger(description='target end gravity'),
        'actual_end_gravity': NullableInteger(description='actual end gravity'),
        'brew_steps': fields.List(fields.Nested(brew_step)),
    })
