from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['SECRET_KEY'] = SECRET_KEY
from app import views
