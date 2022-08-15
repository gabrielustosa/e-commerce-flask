from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(255), unique=True)
    products = db.relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(20), default='default.jpg')
    slug = db.Column(db.String(255), unique=True)
    price = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)

    def __str__(self):
        return self.name
