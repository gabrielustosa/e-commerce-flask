from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    postal_code = StringField('Código Postal', validators=[DataRequired()])
    address = StringField('Endereço', validators=[DataRequired()])
    number = StringField('Número', validators=[DataRequired()])
    complement = StringField('Complemento', validators=[DataRequired()])
    city = StringField('Cidade', validators=[DataRequired()])
    state = StringField('Estado', validators=[DataRequired()])
    submit = SubmitField('Salvar')


class CardForm(FlaskForm):
    number = StringField('Número do Cartão', validators=[DataRequired()])
    expiration_date = StringField('Data de válidade', validators=[DataRequired()])
    cvv = StringField('CVV', validators=[DataRequired()])
    submit = SubmitField('Concluir')

