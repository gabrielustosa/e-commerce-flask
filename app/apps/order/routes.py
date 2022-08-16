from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

from app import db
from app.apps.cart.cart import Cart
from app.apps.order.forms import AddressForm, CardForm
from app.apps.order.models import Address, Order, OrderItem
from app.utils import get_attributes_from_form, get_alert_color

order = Blueprint('order', __name__)


@order.route('/checkout/address', methods=['GET', 'POST'])
def checkout_address():
    form = AddressForm()

    if form.validate_on_submit():
        address = Address(user_id=current_user.id, **get_attributes_from_form(form, Address))

        db.session.add(address)
        db.session.commit()

        return redirect(url_for('order.checkout', address_id=address.id))

    addresses = Address.query.filter_by(user_id=current_user.id)
    return render_template('order/checkout_address.html', form=form, addresses=addresses)


@order.route('/checkout/<address_id>', methods=['GET', 'POST'])
def checkout(address_id):
    form = CardForm()

    cart = Cart()

    cart.clear()

    if form.validate_on_submit():
        order_object = Order(user_id=current_user.id, address_id=address_id, paid=True)

        db.session.add(order_object)

        for item in cart:
            product_id = item['product'].id
            quantity = item['quantity']
            order_item = OrderItem(order_id=order_object.id, product_id=product_id, quantity=quantity)
            db.session.add(order_item)

        db.session.commit()

        cart.clear()

        flash('Compra aprovada!', get_alert_color('success'))

        return redirect('/')

    return render_template('order/checkout.html', form=form, address_id=address_id, cart=cart)
