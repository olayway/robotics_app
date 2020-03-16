from flask import Blueprint, render_template, request
from .models import RegForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            existing_user = User.objects.get(username=form.username.data)
            if existing_user is None:
                hashpass = generate_password_hash(form.password.data, method='sha256')
                user = User(request.form.to_dict())
                user.save()
                login_user(user)
                return redirect(url_for('logged_in'))
    return render_template('register.html', form=form)
