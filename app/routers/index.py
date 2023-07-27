from flask import Blueprint, render_template, render_template_string, jsonify
from mongoengine.errors import ValidationError
from app.forms.url_form import URLForm
from app.models.short_urls import URL
from app.utils.random import generate_random_string


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
def process_origin_url():
    form = URLForm()

    if form.validate_on_submit():
        origin_url = form.origin_url
        url = URL.objects(origin_url=origin_url).first()

        if url:
            temp = render_template_string(
                '_url_table.html',
                url=url
            )
            return jsonify(
                {
                    'message': temp
                }
            )

        try:
            url = URL(
                origin_url=origin_url,
                short_url = generate_random_string()
                )
            url.save()
            temp = render_template_string(
                '_url_table.html',
                url=url
            )

            return jsonify(
                {
                    'message': temp
                }
            )

        except ValidationError as e:

            return jsonify(
                {
                    'message': e.message
                }
            )

    return jsonify(
        {
            'message': 'Invalid inputs'
        }
    ), 400
