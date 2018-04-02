from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from vistoriar.application import app, db


def load_models():
    pass

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    load_models()
    manager.run()
