from flask import Flask, request

app = Flask(__name__)

@app.route('/get/')
def zapros():
    if level := request.args.get('level'):
        text = f'Уровень = {level}'
    else:
        text = 'Приветик!'
    return f'{text} {request.args}'

@app.post('/post/')
def post():
    name = request.form.get('name')
    return f'Hello {name}'


if __name__ == '__main__':
    app.run()