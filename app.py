from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Amit de',
        'title': 'Blog post 1',
        'date': 'March 20, 2019',
        'content': 'First post ever'
    },
    {
        'author': 'Amit ka',
        'title': 'Blog post 2',
        'date': 'March 30, 2019',
        'content': 'Second post ever'
    }
]


@app.route("/")
def hello():
    return "<h1>Sht !<h1>"


@app.route("/home")
def home():
    return render_template('index.html', amits=posts, title='My Home')


@app.route("/about")
def about():
    return render_template('about.html', title='My About ')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)

