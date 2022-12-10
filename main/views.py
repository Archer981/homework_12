from flask import Blueprint, render_template, request
from utils import *


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    posts = find_posts(s)
    return render_template('post_list.html', posts=posts, search_request=s)
