from flask import Blueprint, render_template, request, redirect, url_for

from app.apps.cart.cart import Cart

cart = Blueprint('cart', __name__)


@cart.route('/cart')
def cart_view():
    user_cart = Cart()

    return render_template('cart/view.html', cart=user_cart)


@cart.route('/cart/add/<product_id>', methods=['GET', 'POST'])
def cart_add(product_id):
    user_cart = Cart()

    user_cart.add(product_id, quantity=int(request.args.get('quantity', 1)))

    return redirect(url_for('cart.cart_view'))


@cart.route('/cart/remove/<product_id>')
def cart_remove(product_id):
    user_cart = Cart()

    user_cart.remove(product_id, quantity=int(request.args.get('quantity', 1)))

    return redirect(url_for('cart.cart_view'))


@cart.route('/cart/increment/<product_id>')
def cart_increment(product_id):
    user_cart = Cart()

    user_cart.add(product_id, quantity=int(request.args.get('quantity', 1)))

    return redirect(url_for('cart.cart_view'))


@cart.route('/cart/delete/<product_id>')
def cart_delete(product_id):
    user_cart = Cart()

    user_cart.delete(product_id)

    return redirect(url_for('cart.cart_view'))
