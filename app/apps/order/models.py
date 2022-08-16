from app import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    postal_code = db.Column(db.String(20))
    address = db.Column(db.String(200))
    number = db.Column(db.String(10))
    complement = db.Column(db.String(20))
    city = db.Column(db.String(80))
    state = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order = db.relationship('Order', backref='address', lazy=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    paid = db.Column(db.Boolean)
    order_item = db.relationship('OrderItem', backref='items', lazy=True)

    def __str__(self):
        return self.paid


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer)
