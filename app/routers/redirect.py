from flask import Blueprint, redirect, url_for
from app.models.short_urls import URL


blue_print = Blueprint(
    name='redirect',
    import_name=__name__,
)


@blue_print.get('/')
def root():
    return redirect(url_for('index.index_page'))


@blue_print.get('/<string:short_url>')
def process_short_url(short_url):
    url = URL.objects(short_url=short_url).first()
    origin_url= url.origin_url
    url.total_visit += 1
    url.save()
    return redirect(origin_url)
