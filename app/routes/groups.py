from flask import Blueprint, request, jsonify
from app.services.database import db
import os, datetime
from twilio.rest import Client
from dotenv import load_dotenv

groups_bp = Blueprint('groups', __name__)

@groups_bp.route('/groups', methods=['GET'])
def get_groups():
    user_cell = request.args.get('user_cell')
    try:
        groups = list(db["groups"].find({"members": user_cell}))
    except Exception as e:
        return jsonify({"error": e})
    
    for group in groups:
        group['_id'] = str(group['_id'])
    return jsonify(groups), 200


@groups_bp.route('/groups', methods=['POST'])
def add_group():
    data = request.json
    project_name = data.get('project-name')
    members = data.get('members')
    members_info = []
    try:
        users = list(db["users"].find({}))
    except Exception as e:
        return jsonify({"error": e})
    
    for user in users:
        if user["name"] in members:
            members_info.append(user)
    date = datetime.datetime.now()
    new_group = {"name": project_name, "members": members, "created_date": date}
    load_dotenv() 
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    try:
        db["groups"].insert_one(new_group)
        for member in members_info:
            cell = member[cell]
            cell[0] = "+27"
            message = client.messages.create(
                body=f"You have been added to group {project_name}. Your group members are {members}",
                from_=os.getenv("TWILIO_NUMBER"),
                to = cell,
                )
            print(message.body)
        return jsonify({"message": "Group created successfully"}), 201
    except Exception as e:
        return jsonify({"error": e})
