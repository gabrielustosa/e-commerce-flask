from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship('Product', backref='owner', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        serial = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return serial.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        serial = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = serial.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)

    def __str__(self):
        return f'User({self.username})'
