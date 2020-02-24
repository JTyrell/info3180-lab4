from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    pitcha = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png','jpeg','gif','tiff','jfif','and other Images only!'])
])
