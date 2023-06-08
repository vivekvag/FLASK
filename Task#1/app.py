from markupsafe import escape
from flask import Flask, render_template, abort, request, url_for, flash, redirect
from forms import CourseForm
import os, datetime

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '547f8a995c7b4ca6d44442005632cec674b55f300a9cd240'

# Courses List
courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/')
def index():
    return render_template('index.html', courses_list=courses_list)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    form = CourseForm()
    if form.validate_on_submit():
        courses_list.append({'title': form.title.data,
                             'description': form.description.data,
                             'price': form.price.data,
                             'available': form.available.data,
                             'level': form.level.data
                             })
        return redirect(url_for('index'))
    return render_template('create.html', form=form)

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