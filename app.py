from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager


app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'images'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'u\xaa_\xf8N^\x98\x1f\xeb\xe1\x0cg\x1f\x0e%\xe1\xb7\x05D\x03\xdf\xc8}\x85'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
configure_uploads(app, photos)


# Add function into the templates
@app.template_filter('time_since')
def time_since(delta):
    seconds = delta.total_seconds()

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        return '%dd' % days
    elif hours > 0:
        return '%dh' % hours
    elif minutes > 0:
        return '%dm' % minutes
    else:
        return 'Just now'


from views import *

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
