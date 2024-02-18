from pathlib import PurePath, Path
from flask import Flask, make_response, render_template, request, abort, redirect, session, url_for, flash
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = b'8b768b83dffc8e4b84cf0a79105e29c2bb0445e6b42c3b4075b97cb752f81b32' 

# GET и POST методы

@app.route('/get/')
def zapros():
    #GET метод
    if level := request.args.get('level'):
        text = f'Уровень = {level}'
    else:
        text = 'Приветик!'
    return f'{text} {request.args}'

@app.route('/post/', methods=['GET', 'POST'])
def post():
    # POST метод
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        flash('Успешно') # Всплывающее сообщение прикреплении файла
        return redirect(url_for('post'))
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    # Создание страницы для ошибки 404
    return render_template('404.html'), 404

# Перенаправление

@app.route('/redir/')
def redirect_to():
    # Перенаправление на другую страницу
    return redirect(url_for('post'))

@app.route('/external/')
def ext_redir():
    # Перенаправление на другой сайт
    return redirect(url_for('https://vk.com/'))

# Cookie-файлы

@app.route('/c/')
def cookiez():
    response = make_response("cookie установлен")
    response.set_cookie('username', 'admin')
    return response

@app.route('/getname/')
def get_name():
    name = request.cookies.get('username')
    return f'имя: {name}'

# Сессии

@app.route('/s/')
def sessions():
    if 'username' in session:
        return f'Привет, {session['username']}'
    else:
        return redirect(url_for('login'))
    
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or'NoName'
        return redirect(url_for('sessions'))
    return render_template('username_form.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
