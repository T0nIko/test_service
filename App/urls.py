from App.views import IndexView, ApiView


def plug_urls(app):
    app.add_url_rule(
        '/',
        view_func=IndexView.as_view(name='index')
    )

    api_view = ApiView.as_view('user_api')

    app.add_url_rule(
        '/api/v1/users',
        view_func=api_view,
        methods=[
            'GET',
        ],
        defaults = {
            'query': None
        }
    )
    app.add_url_rule(
        '/api/v1/users/<query>',
        view_func=api_view,

    )