from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db

application = create_app('prod')

application.register_blueprint(blueprint)

application.app_context().push()

manager = Manager(application)

migrate = Migrate(application, db, directory='../migrations')

# apply any/all pending migrations.
with application.app_context():
    from flask_migrate import upgrade as _upgrade
    _upgrade()

manager.add_command('db', MigrateCommand)
