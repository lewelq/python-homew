from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = b'8b768b83dffc8e4b84cf0a79105e29c2bb0445e6b42c3b4075b97cb752f81b32' 


@app.route('/', methods=['GET', 'POST'])
def forma():
    if request.method == 'POST':
        session['email'] = request.form.get('email')
        session['username'] = request.form.get('username')
        return redirect(url_for('login'))
    return render_template('abc.html')

@app.route('/login/')
def login():
    if 'username' and 'email' in session:
        return f'Почта: {session["email"]} <br> Имя: {session["username"]} <br>'\
        f'<button><a href="/logout/">Выйти</a></button>'  # Обновленная кнопка выхода
    else:
        return redirect(url_for('forma'))

@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('forma'))
    
if __name__ == '__main__':
    app.run(debug=True)