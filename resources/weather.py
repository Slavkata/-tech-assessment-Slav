from flask import jsonify
from flask_restful import Resource, reqparse

from models.weather import Weather

class WheatherResource(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument('time')
        self.parser.add_argument('temp')

        data = self.parser.parse_args()

        record = Weather.query.filter_by(time=data.time).first()
        if record is None:
            try:
                weather = Weather(data.time, data.temp)
                weather.save_to_db()
                return jsonify(weather.serialize())
            except Exception as e:
                return {'message': e}, 400
        else:
            record.update_in_db(data.temp)

    def get(self):
        try:
            return jsonify(Weather.get_all(self))
        except Exception as e:
            return {"message": e}, 404