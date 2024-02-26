from flask import Flask, render_template, request, url_for
from models import db, User, Post, Comment
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'examplekey'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("fill-db")
def fill_tables():
    count = 5
    for user in range(1, count + 1):
        new_user = User(username = f'user{user}', email = f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()

    for post in range(1, count ** 2):
        author = User.query.filter_by(username = f'user{post % count + 1}').first()
        new_post = Post(title = f'post title {post}', content = f'post content {post}', author = author)
        db.session.add(new_post)
    db.session.commit()

@app.cli.command("add-john")
def add_user():
    user = User(username = 'John', email = '123@xx.com')
    db.session.add(user)
    db.session.commit()
    print('success')

@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username = 'John').first()
    user.email = 'newemail@xx.com'
    db.session.commit()
    print('success')

@app.cli.command("delete-john")
def delete_user():
    user = User.query.filter_by(username = 'John').first()
    db.session.delete(user)
    db.session.commit()
    print('success')

@app.route('/')
def index():
    return 'Hi'

@app.route('/data/')
def data():
    return 'Your data'

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)

@app.route('/users/<username>')
def filter_users(username):
    users = User.query.filter(User.username == username).first()
    context = {'users': users}
    return render_template('users.html', **context)

class LoginForm(FlaskForm):
    name = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])

class RegisterForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    age = IntegerField('Age', validators = [DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'мужчина'), ('female', 'женщина')])

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 6)])
    confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

@app.route('/login/')
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form = form)

@app.route('/register/')
def reg():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('reg.html', form = form)


if __name__ == '__main__':
    app.run(debug = True)
    