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

    image = api.model('Image', {
        'id': fields.String(attribute='id'),
        'parent_id': fields.String(attribute='parent_id'),
        'url': fields.String(required=True, attribute='url'),
        'created': fields.DateTime(attribute='created'),
    })

    brew = api.model('brew', {
        'id': NullableInteger(description='brew identifier'),
        'brew_name': fields.String(required=True, description='brew name'),
        'brew_type': fields.String(required=True, description='brew type'),
        'created': fields.DateTime(description='brew date'),
        'brewsters': NullableString(description='who brewed the brew'),
        'location': NullableString(description='where was it brewed'),
        'recipe': NullableString(description='link to recipe'),
        'tilt_url': NullableString(description='tilt url'),
        'description': NullableString(description='description'),
        'target_start_gravity': NullableInteger(description='target start gravity'),
        'actual_start_gravity': NullableInteger(description='actual start gravity'),
        'target_end_gravity': NullableInteger(description='target end gravity'),
        'actual_end_gravity': NullableInteger(description='actual end gravity'),
        'images': fields.List(fields.Nested(image)),
    })


class BrewStepDto:

    api = Namespace('brew step', description='step related operations')

    step = api.model('step', {
        'id': NullableInteger(description='step identifier'),
        'parent_id': NullableInteger(description='parent identifier'),
        'next_step': NullableInteger(description='id of next step'),
        'index': NullableInteger(description='index'),
        'name': fields.String(required=True, description='step name'),
        'description': NullableString(description='description'),
        'started': fields.DateTime(description='started timestamp'),
        'ended': fields.DateTime(description='ended timestamp'),
    })
