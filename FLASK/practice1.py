from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'
    #return 48

@app.route('/Дмитрий/')
def dima():
    return 'Здравствуйте, Дмитрий'


if __name__ == '__main__':
    app.run()