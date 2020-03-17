from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash

from .models import User
from .forms import RegForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm(request.form)
    print('test_register')
    if request.method == 'POST':
        print('POST')
        try:
            assert form.validate(), 'Registration failed'
        except AssertionError as error:
            print(error)
        else:
            try:
                User.objects.get(username=form.username.data)
            except:
                print('new user')
                user = User(username=form.username.data,
                            email=form.email.data)
                user.set_password(form.password.data)
                user.save()
                login_user(user)
            ### tbd - handler for already registered users
            return redirect(url_for('auth.loggedin'))
    return render_template('register.html', 
                            title='Create an Account.', 
                            form=form)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.loggedin'))

    form = LoginForm(request.form)

    if request.method == 'POST':
        try:
            assert form.validate(), 'Login Failed'
        except AssertionError as error:
            print(error)
        else:
            username = form.username.data
            password = form.password.data
            print(username)
            print(password)
            try:
                user = User.objects.get(username=username)
            except:
                print('User not registered')
            else:
                print('REGISTERED')
                if user.check_password(password=password):
                    login_user(user)
                    next_url = request.args.get('next')[1:]
                    if next_url:
                        return redirect(url_for('auth.{}'.format(next_url)))
                    return redirect(url_for('auth.loggedin'))

    return render_template('login.html', form=form)



@auth.route('/loggedin')
@login_required
def loggedin():
    return render_template('loggedin.html', name=current_user.username)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/mycases')
@login_required
def mycases():
    return render_template('mycases.html', name=current_user.username)