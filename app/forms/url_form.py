from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms.validators import URL,DataRequired

class URLForm(FlaskForm):
    origin_url = URLField(
        'Origin URL',
        validators=[
            URL(),
            DataRequired()
        ]
    )