from .app import db

class Camper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    signups = db.relationship("Signup", backref="camper", cascade="all, delete-orphan")

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer)
    signups = db.relationship("Signup", backref="activity", cascade="all, delete-orphan")

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable=False)
    camper_id = db.Column(db.Integer, db.ForeignKey("camper.id"), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
