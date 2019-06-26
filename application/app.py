from flask import Flask

from .configuration import config
from .extensions import login_manager, flask_db
from .models import User


def create_app(config_name):
    """Creates the app."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    configure_extensions(app)
    configure_blueprints(app)

    return app


def configure_extensions(app):
    """Configures the extensions."""

    flask_db.init_app(app)

    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'bp_auth.login'
    login_manager.login_message = '请登录'
    login_manager.login_message_category = 'error'
    login_manager.needs_refresh_message = '请重新登录'
    login_manager.needs_refresh_message_category = 'error'

    @login_manager.user_loader
    def load_user(id):
        return User.get_or_none(User.id == id)


def configure_blueprints(app):
    from .misc import bp_misc
    app.register_blueprint(bp_misc, url_prefix='/misc')

    from .auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    from .welcome import bp_welcome
    app.register_blueprint(bp_welcome, url_prefix='/welcome')

    from .user import bp_user
    app.register_blueprint(bp_user, url_prefix='/user')

    from application.corpsum import bp_corpsum
    app.register_blueprint(bp_corpsum, url_prefix='/corpsum')

    from application.cvinfo import bp_cvinfo
    app.register_blueprint(bp_cvinfo, url_prefix='/cvinfo')
