from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Sign Up')
class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remeber me')
	submit=SubmitField('Login')
class ReviewForm(FlaskForm):
	rating = StringField('Rating', validators=[DataRequired(), Length(min=1, max=2, message=('Rating should be between 0 and 10.'))])
	review = StringField('Review', validators=[DataRequired()])
	submit = SubmitField('Submit')