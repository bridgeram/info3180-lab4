from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    upload = FileField('Image', validators=[FileRequired('Please upload your file here'), FileAllowed(['jpg', 'png'], 'Images only!')])