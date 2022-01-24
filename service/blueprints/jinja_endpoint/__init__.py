from flask import Blueprint, request, render_template

blueprint = Blueprint('rotate_img', __name__, url_prefix='/rotate_img')

@blueprint.route('')
def get_template():
    return render_template('example.html')