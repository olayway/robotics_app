from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, InputRequired


class LoginForm(Form):
    """User Login Form"""

    username = StringField('Username', 
                validators=[
                    DataRequired()
                ])

    password = PasswordField('Password', 
                validators=[
                    DataRequired(), 
                    Length(
                        min=3, 
                        message='Select a stronger password.'
                    )
                ])

    # submit = SubmitField('Log In')

class RegForm(LoginForm):
    """User Registration Form"""

    email = StringField('Email', 
                validators=[
                    DataRequired(), 
                    Length(
                        min=3, 
                        message='Enter a valid email.')
                ])

    # confirm = PasswordField('Confirm Your Password',
    #             validators=[
    #                 DataRequired(), 
    #                 EqualTo(
    #                     'password', 
    #                     message='Passwords must match.'
    #                 )
    #             ])

    # accept_rules = BooleanField('I accept the site rules.',
    #                 validators=[
    #                     InputRequired()
    #             ])

    # submit = SubmitField('Register')

