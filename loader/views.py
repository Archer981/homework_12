from flask import Blueprint, render_template, request

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/add_post')
def add_post_page():

    return render_template('post_form.html')
