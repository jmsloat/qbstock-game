from flask import Flask
from flask import render_template

from db import quarterbacks

app = Flask(__name__)


@app.route('/')
def hello_world():
    all = quarterbacks.QuarterbackRepository().get_all()

    return render_template('index.html', quarterbacks=all)

@app.route('/transaction')
def transaction():
    all = quarterbacks.QuarterbackRepository().get_all()
    return render_template('transaction.html', quarterbacks = all)


if __name__ == '__main__':
    app.run()
