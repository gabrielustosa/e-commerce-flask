from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    description = TextAreaField('Descrição', validators=[DataRequired()])
    category = SelectField('Categoria', coerce=int)
    image = FileField('Imagem', validators=[FileAllowed(['jpg', 'png'])])
    price = FloatField('Preço', validators=[DataRequired()])
    stock = IntegerField('Estoque', validators=[DataRequired()])
    submit = SubmitField('Criar')


class CategoryForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Criar')
