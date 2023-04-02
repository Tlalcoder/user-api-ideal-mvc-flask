from source.controllers.user_controller import user_blueprint
from source.controllers.root_controller import root_blueprint


def register_blueprints(app):
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(root_blueprint)