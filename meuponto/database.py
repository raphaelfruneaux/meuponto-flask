from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TimestampMixin(object):
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated = db.Column(db.DateTime, nullable=False, onupdate=datetime.now)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def json(self):
        """
        Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime) else value.strftime('%Y-%m-%d')
            for column, value in self.__dict__.items()
        }