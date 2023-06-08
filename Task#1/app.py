from markupsafe import escape
from flask import Flask, render_template, abort, request, url_for, flash, redirect
import os, datetime

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '547f8a995c7b4ca6d44442005632cec674b55f300a9cd240'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]
@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]
    return render_template('comments.html', comments=comments)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')

# NOT Required
# @app.route('/capitalize/<word>/')
# def capitalize(word):
#     return '<h1> Hey, {} !!</h1>'.format(escape(word.capitalize()))

# @app.route('/add/<int:n1>/<int:n2>/')
# def add(n1, n2):
#     return '<h1>{}</h1>'.format(n1 + n2)

# @app.route('/hello/')
# def hello():
#     return render_template('hello.html' , utc_dt=datetime.datetime.utcnow())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)