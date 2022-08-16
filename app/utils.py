import os
import secrets
import unicodedata
import re

from PIL import Image
from flask import url_for, current_app
from flask_mail import Message

from app import mail
from app.config import BASE_DIR


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@gabrielustosa.com.br', recipients=[user.email])
    message.body = f'''
        To reset your password, visit the following link {url_for('auth.reset_password', token=token, _external=True)}
    '''
    mail.send(message)


def save_picture(form_picture, path):
    random_hex = secrets.token_hex(10)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = BASE_DIR / current_app.static_folder / 'images' / path / picture_fn

    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return f'images/{path}/{picture_fn}'


def get_alert_color(category):
    categories = {
        'error': 'text-red-700 bg-red-100',
        'success': 'text-green-700 bg-green-100',
        'info': 'text-blue-700 bg-blue-100',
        'warning': 'text-yellow-700 bg-yellow-100',
        'alert': 'text-gray-700 bg-gray-200',
    }
    return categories[category]


def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower()).strip()
    return re.sub(r'[-\s]+', '-', value)


def get_slug(value, model):
    slug = slugify(value)
    if model.query.filter_by(slug=slug).scalar():
        random_hex = secrets.token_hex(5)
        slug += f'-{random_hex}'
    return slug


def get_attributes_from_form(form, model, exclude=None):
    if not exclude:
        exclude = []
    variables = [var for var in vars(model).keys() if not var.startswith('_')]
    for var in variables:
        try:
            getattr(form, var)
        except AttributeError:
            exclude.append(var)
    return {var: getattr(form, var).data for var in variables if var not in exclude}
