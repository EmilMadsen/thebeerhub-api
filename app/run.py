import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db

# TODO: run as something else.
application = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

application.register_blueprint(blueprint)

application.app_context().push()

manager = Manager(application)

migrate = Migrate(application, db)

manager.add_command('db', MigrateCommand)
