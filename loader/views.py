from flask import Blueprint, render_template, request
from loader.utils import *
from main.utils import save_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/add_post')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/upload_post', methods=['POST'])
def upload_post_page():
    picture = request.files.get('picture')
    post = request.form.get('content')
    picture_path = save_picture(picture)
    save_post(picture_path, post)
    return render_template('post_uploaded.html', picture=picture_path, post=post)
