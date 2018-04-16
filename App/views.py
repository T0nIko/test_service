from flask.views import MethodView
from flask import request, render_template, redirect, url_for

import json


class IndexView(MethodView):
    template_name = 'App/index.html'

    def get(self):
        return render_template(self.template_name)


class ApiView(MethodView):
    def get(self, query):
        print(query)
        return redirect(url_for('index'))

