from flask import render_template, Blueprint

from app import Product

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)
