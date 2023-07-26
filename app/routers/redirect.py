from flask import Blueprint


blue_print = Blueprint(
    name='redirect',
    import_name=__name__,
)


@blue_print.get('/<string:short_url>')
def process_short_url(short_url):
    pass

