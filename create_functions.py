import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(__name__, config):
    # initialize the app and the db
    app = Flask(__name__)
    app.config.from_object(__name__)
    for key in config['Flask_Settings']:
        app.config[key.upper()] = config['Flask_Settings'][key]
    return app


def create_table_repr(app):
    db = SQLAlchemy(app)

    class Users(db.Model):
        user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String)
        password = db.Column(db.String)
        theta = db.Column(db.Float, default=0)
        k = db.Column(db.Float, default=0)

        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return '<User %r>' % self.username

    """
        class Items(db.Model):
            item_id = db.Column(db.String, primary_key=True)
            question = db.Column(db.String)
            theta = db.Column(db.Float, default=0)
            k = db.Column(db.Float, default=0)

            def __init__(self, item_id, question):
                self.item_id = item_id
                self.question = question

            def __repr__(self):
                return 'ItemId: {}, Question: {}'.format(self.item_id, self.question)
    """

    class Events(db.Model):
        event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        event_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
        item_id = db.Column(db.Integer)
        user_id = db.Column(db.Integer)
        theta_before = db.Column(db.Float)
        theta_after = db.Column(db.Float)
        answered = db.Column(db.Integer)
        k = db.Column(db.Float, default=0)

        def __init__(self, item_id, user_id, theta_before, theta_after, answered, k):
            self.item_id = item_id
            self.user_id = user_id
            self.theta_after = theta_after
            self.theta_before = theta_before
            self.answered = answered
            self.k = k

        def __repr__(self):
            return 'Event_id: {}'.format(self.event_id)

    return db, Users, Events
