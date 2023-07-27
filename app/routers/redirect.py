from flask import Blueprint, redirect, url_for

blue_print = Blueprint(
    name='redirect',
    import_name=__name__,
)


@blue_print.get('/')
def root():
    return redirect(url_for('index.index_page'))


@blue_print.get('/<string:short_url>')
def process_short_url(short_url):
    pass
