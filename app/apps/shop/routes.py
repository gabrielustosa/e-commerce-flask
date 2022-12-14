import secrets

from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

from app import Product, db, Category
from app.utils import save_picture, get_slug
from app.apps.shop.forms import ProductForm, CategoryForm

shop = Blueprint('shop', __name__)


@shop.route('/category/create/', methods=['GET', 'POST'])
@login_required
def create_category():
    form = CategoryForm()

    if form.validate_on_submit():
        category = Category(name=form.name.data, slug=get_slug(form.name.data, Category))

        db.session.add(category)
        db.session.commit()

        return redirect('/')

    return render_template('category/create.html', form=form)


@shop.route('/product/create/', methods=['GET', 'POST'])
@login_required
def create_product():
    form = ProductForm()
    form.category.choices = [(category.id, category.name) for category in Category.query.all()]

    if form.validate_on_submit():

        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            stock=form.stock.data,
            slug=get_slug(form.name.data, Product),
            user_id=current_user.id,
            category_id=form.category.data
        )
        if form.image.data:
            picture_file = save_picture(form.image.data, 'products')
            product.image = picture_file

        db.session.add(product)
        db.session.commit()
        return redirect('/')

    return render_template('product/create.html', form=form)


@shop.route('/product/<product_slug>')
def view_product(product_slug):
    product = Product.query.filter_by(slug=product_slug).first_or_404()
    quantities = (n for n in range(1, 21))
    return render_template('product/view.html', product=product, quantities=quantities)


@shop.route('/category/<category_id>')
def view_category(category_id):
    products = Product.query.filter_by(category_id=category_id)

    return render_template('home.html', products=products)


@shop.app_context_processor
def inject_categories():
    return {
        'categories': Category.query.all()
    }
