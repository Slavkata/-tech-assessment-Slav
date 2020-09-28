from flask import Flask
from flask_restful import Api
from models.db_init import db
from flask_apscheduler import APScheduler
from crawler import request_page
from flask import render_template

# from resources.dummy import DummiesResource
from resources.weather import WheatherResource


app = Flask(__name__)
api = Api(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

url = 'https://www.weather-forecast.com/weather-stations/Eindhoven-Airport'

app.apscheduler.add_job(func=request_page, trigger='interval', args=[url], id='1', minutes=5)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:slavkata@localhost/tech_assignment'

# api.add_resource(DummiesResource, '/dummy/')
api.add_resource(WheatherResource, '/weather/')

@app.route("/weather/t", methods=['GET'])
def show_weather():
    data = WheatherResource().get().json
    return render_template('index.html', data=data)


db.init_app(app)
