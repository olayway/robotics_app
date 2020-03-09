from flask import Blueprint, render_template

test_page = Blueprint('test_page', __name__, 
template_folder='templates')

@test_page.route('/')
# @test_page.route('/<id>')
def test():
    return render_template('index.html')