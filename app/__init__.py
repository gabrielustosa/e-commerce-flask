from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate

from app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
mail = Mail()
migrate = Migrate()


def create_app(config_class=Config):
    instance_config = Config()
    app = Flask(__name__, template_folder=instance_config.TEMPLATE_FOLDER, static_folder=instance_config.STATIC_FOLDER)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from app.apps.auth.routes import auth
    from app.apps.main.routes import main
    from app.apps.shop.routes import shop
    from app.apps.cart.routes import cart
    from app.apps.order.routes import order
    from app.errors.handlers import errors

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(shop)
    app.register_blueprint(cart)
    app.register_blueprint(order)
    app.register_blueprint(errors)

    return app


from app.apps.shop.models import Category, Product
from app.apps.order.models import Order, OrderItem
