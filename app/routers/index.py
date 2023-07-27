from flask import Blueprint, render_template, render_template_string, jsonify
from app.forms.url_form import URLForm


blue_print = Blueprint(
    name='index',
    import_name=__name__,
    url_prefix='/home',
    template_folder='../templates'
)


@blue_print.get('/')
def index_page():
    form = URLForm()
    return render_template(
        template_name_or_list='index.html',
        form=form
    )


@blue_print.post('/')
def process_origin_url(origin_url):
    pass
