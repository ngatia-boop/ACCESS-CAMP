from flask import request, jsonify
from .app import app, db
from .models import Camper, Activity, Signup

@app.get("/campers")
def get_campers():
    campers = Camper.query.all()
    return jsonify([{"id": c.id, "name": c.name, "age": c.age} for c in campers]), 200
