from flask import Blueprint, render_template, request
from main.utils import *


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('substr', '')
    posts = find_posts(substr)
    return render_template('post_list.html', posts=posts, search_request=substr)
