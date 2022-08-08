from flask import Flask
from config import DevelopmentConfig
from api import api_bp
from database import setup as setup_db, init_db_command


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(api_bp)
    app.cli.add_command(init_db_command)
    setup_db(app)

    return app


if __name__ == '__main__':
    create_app().run()
