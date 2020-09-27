from flask import jsonify
from flask_restful import Resource, reqparse

from models.dummy import Dummy


class DummiesResource(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument('year', type=int)
        data = self.parser.parse_args()

        try:
            dummy = Dummy(data.year)
            dummy.save_to_db()
            return jsonify(dummy.serialize())
        except Exception as e:
            return {'message': e}, 400

    def get(self):
        try:
            return jsonify(Dummy.get_all(self))
        except Exception as e:
            return {"message": e.__repr__()}, 404