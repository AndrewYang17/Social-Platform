from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import InputRequired, Length
from flask_uploads import IMAGES


class RegisterForm(FlaskForm):
    name = StringField('Full name', validators=[InputRequired('A full name is required.'),
                                                Length(max=100,
                                                       message='Your name can\'t be more than 100 characters.')])
    username = StringField('Username', validators=[InputRequired('Username is required.'),
                                                   Length(max=30,
                                                          message='Username can\'t be more than 30 characters')])
    password = PasswordField('Password', validators=[InputRequired('A password is required.')])
    image = FileField(validators=[FileAllowed(IMAGES, 'Only images are accepted.'),
                                  InputRequired('Input your image.')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Username is required.')])
    password = PasswordField('Password', validators=[InputRequired('Password is required.')])
    remember = BooleanField('Remember me')


class TweetForm(FlaskForm):
    text = TextAreaField('Message', validators=[InputRequired('Message is required.')])