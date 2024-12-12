from flask import request, Blueprint
from app.services.database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name')
    cell = data.get('cell')
    user = db["Users"].find_one({"name": name, "cell": cell})
    if user:
        return user
    return 