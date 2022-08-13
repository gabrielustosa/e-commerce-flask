from flask import url_for
from flask_mail import Message

from app import mail


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@gabrielustosa.com.br', recipients=[user.email])
    message.body = f'''
        To reset your password, visit the following link {url_for('auth.reset_password', token=token, _external=True)}
    '''
    mail.send(message)


def get_alert_color(category):
    categories = {
        'error': 'text-red-700 bg-red-100',
        'success': 'text-green-700 bg-green-100',
        'info': 'text-blue-700 bg-blue-100',
        'warning': 'text-yellow-700 bg-yellow-100',
        'alert': 'text-gray-700 bg-gray-200',
    }
    return categories[category]
