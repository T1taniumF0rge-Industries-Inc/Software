#hello
from flask import Flask

app = Flask(__name__)

from markupsafe import escape
from flask import render_template
@app.route("/")
def mainpage():
    return render_template('mainpage.html')
@app.route("/user/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
@app.route("/buycomputer/")
def test():
    return render_template('test.html')
@app.route("/htmltest")
def html1():
    return render_template('test.html')