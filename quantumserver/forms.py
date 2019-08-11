from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from quantumserver.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=200)])
    email = StringField('Email',validators=[DataRequired(), Email(), Length(max=500)])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken')

class LoginForm(FlaskForm):
    #username = StringField('Username',validators=[DataRequired(), Length(min=2, max=200)])
    email = StringField('Email',validators=[DataRequired(), Email(), Length(max=500)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    #confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Login')
