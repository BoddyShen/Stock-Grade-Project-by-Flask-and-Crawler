import os
from flask import Flask

from root.globals import db, login_manager
from root.users.views import users
from root.core.views import core


def create_app():
    """Create the flask application"""

    # Initiate app
    app = Flask(__name__)

    # Update app.config from environment variables
    app.config["SECRET_KEY"] = os.urandom(16)
    app.config["MONGODB_SETTINGS"] = {
        "authentication_source": "admin",
        "host": os.getenv("MONGODB_HOST"),
        "port": int(os.getenv("MONGODB_PORT")),
        "username": os.getenv("MONGODB_USERNAME"),
        "password": os.getenv("MONGODB_PASSWORD"),
    }

    # format(username, password
    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(users, url_prefix="/users")

    # initialize database

    db.init_app(app)
    print("MongoDB'connection is built.")
    # initialize login manager
    login_manager.init_app(app)
    # 導向的view
    login_manager.login_view = "users.login"

    return app
