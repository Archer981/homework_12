from flask import Blueprint, render_template, request, redirect
from main.utils import *


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s', '')
    posts = find_posts(substr)
    if not posts:
        return redirect('/')
    return render_template('post_list.html', posts=posts, search_request=substr)
