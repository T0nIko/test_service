from flask.views import MethodView
from flask import request, render_template, jsonify

from .models import UserModel


class IndexView(MethodView):
    template_name = 'App/index.html'

    def get(self):
        return render_template(self.template_name)


class ApiStringQueryView(MethodView):
    def get(self, query):
        if query is not None:
            params = {
                elem.split('=')[0]: elem.split('=')[1]
                for elem in query.split(',')
            }
            res = UserModel.query.filter_by(**params).all()
        else:
            res = UserModel.query.all()

        return jsonify([obj.serialize for obj in res])


class ApiView(MethodView):
    def post(self):
        if request.json:
            res = UserModel.query.filter_by(**request.json).all()
        else:
            res = UserModel.query.all()

        return jsonify([obj.serialize for obj in res])
