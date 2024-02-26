from flask import Flask, request, render_template, url_for
from models import db, Data
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SECRET_KEY'] = '123123132'
db.init_app(app)
csrf = CSRFProtect(app)
with app.app_context():
    db.create_all()

class Reg_form(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    surname = StringField('Surname', validators = [DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

@app.route('/', methods = ['GET', 'POST'])
def register():
    form = Reg_form()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        data = Data(name = name, surname = surname, password = password, email = email)
        db.session.add(data)
        db.session.commit()
    return render_template('reg.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
