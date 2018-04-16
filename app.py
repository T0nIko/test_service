from flask import Flask

from werkzeug.contrib.fixers import ProxyFix

from App.urls import plug_urls
from App.models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.wsgi_app = ProxyFix(app.wsgi_app)

with app.app_context():
    plug_urls(app)
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run()
