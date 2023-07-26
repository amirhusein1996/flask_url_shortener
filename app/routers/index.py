from flask import Blueprint, render_template

blue_print = Blueprint(
    name='index',
    import_name=__name__,
    url_prefix='/home',
    template_folder='../templates'
)

@blue_print.get('/')
def index_page():
    pass

@blue_print.post('/<path:origin_url')
def process_origin_url(origin_url):
    pass
