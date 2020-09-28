from datetime import datetime

from models.db_init import db

class Weather(db.Model):
    #
    #Make sure to provide a default value when changing from nullable=False to nullable=True
    #
    __tablename__ = 'weathers'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    time = db.Column(db.String(5), nullable=False)
    temp = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, time, temp):
        self.time = time
        self.temp = temp
        self.created_at = datetime.now()

    def update_in_db(self, temp):
        self.temp = temp
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls, id):
        return [x.serialize() for x in cls.query.all()]

    def __repr__(self):
        return self.serialize()

    def serialize(self):
        return {
            'time': self.time,
            'temp': self.temp,
        }