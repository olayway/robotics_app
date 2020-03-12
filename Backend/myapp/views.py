from flask import Blueprint, render_template

test = Blueprint('test_page', __name__, 
template_folder='templates')

@test.route('/')
# @test_page.route('/<id>')
def test():
    return render_template('index.html') 