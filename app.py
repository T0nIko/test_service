from flask import Flask

from App import urls

app = Flask(__name__)

urls.plug_urls(app)

if __name__ == '__main__':
    app.run()
