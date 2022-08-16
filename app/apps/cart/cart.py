from flask import session

from app import Product


class Cart:
    def __init__(self):
        self.cart = session['cart']

    def __iter__(self):
        for product_id, quantity in self.cart.items():
            product = Product.query.get(product_id)
            yield {
                'product': product,
                'quantity': quantity,
                'total_price': quantity * product.price
            }

    def __len__(self):
        return sum(item['quantity'] for item in self)

    @staticmethod
    def save():
        session.modified = True

    def add(self, product_id, quantity=1):
        if product_id not in self.cart:
            self.cart[product_id] = 0

        self.cart[product_id] += quantity
        self.save()

    def remove(self, product_id, quantity=1):
        if product_id in self.cart:
            if self.cart[product_id] > 1:
                self.cart[product_id] = self.cart[product_id] - quantity
            else:
                self.delete(product_id)
            self.save()

    def delete(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        session['cart'] = {}
        self.save()

    def get_total_price(self):
        return sum(item['total_price'] for item in self)
