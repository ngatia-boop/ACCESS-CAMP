from flask import Blueprint, request, jsonify
from ..models import db, Camper

campers_bp = Blueprint('campers', __name__)

@campers_bp.route('', methods=['GET'])
def get_campers():
    campers = Camper.query.all()
    return jsonify([camper.to_dict() for camper in campers]), 200

@campers_bp.route('/<int:id>', methods=['GET'])
def get_camper(id):
    camper = Camper.query.get(id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404
    return jsonify(camper.to_dict(include_signups=True)), 200

@campers_bp.route('', methods=['POST'])
def create_camper():
    try:
        data = request.get_json()
        camper = Camper(
            name=data.get('name'),
            age=data.get('age')
        )
        db.session.add(camper)
        db.session.commit()
        return jsonify(camper.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400

@campers_bp.route('/<int:id>', methods=['PATCH'])
def update_camper(id):
    camper = Camper.query.get(id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404
    
    try:
        data = request.get_json()
        if 'name' in data:
            camper.name = data['name']
        if 'age' in data:
            camper.age = data['age']
        
        db.session.commit()
        return jsonify(camper.to_dict()), 202
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400