import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi from flask'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
