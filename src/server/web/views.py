from flask import send_from_directory, render_template, current_app
from . import main

@main.route('/', defaults={'path': 'index.html'})
@main.route('/<path:path>')
def default(path):
    context = {
        'version': '2'
    }
    return render_template('index.html', **context)