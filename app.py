import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Book


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/name/<name>')
def get_book_name(name):
    return f'name : {name}'


@app.route('/details')
def get_book_details():
    author = request.args.get('author')
    published = request.args.get('published')
    return f'Author : {author}, Published: {published}'


if __name__ == '__main__':
    app.run()
