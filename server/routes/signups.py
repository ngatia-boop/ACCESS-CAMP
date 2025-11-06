from flask import Blueprint, request, jsonify
from ..models import db, Signup

signups_bp = Blueprint('signups', __name__)

@signups_bp.route('', methods=['POST'])
def create_signup():
    try:
        data = request.get_json()
        signup = Signup(
            time=data.get('time'),
            camper_id=data.get('camper_id'),
            activity_id=data.get('activity_id')
        )
        db.session.add(signup)
        db.session.commit()
        return jsonify(signup.to_dict(include_camper=True, include_activity=True)), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400