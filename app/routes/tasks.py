from flask import Blueprint, request, jsonify
from app.services.database import db
import datetime

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    group_id = request.args.get('group_id')
    try:
        tasks = list(db["tasks"].find({"group_id": group_id}))
    except Exception as e:
        return jsonify({"error": e})
    for task in tasks:
        task['_id'] = str(task['_id'])
    return jsonify(tasks), 200

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    group_id = data.get('group_id')
    task_name = data.get('name')
    assigned_to = data.get('assigned_to')
    date = datetime.datetime.now()
    
    new_task = {"group_id": group_id, "name": task_name, "assigned_to": assigned_to, "created_date": date, "status": "not started"}
    try:
        db["tasks"].insert_one(new_task)
    except Exception as e:
        return jsonify({"error":e})
    return jsonify({"message": "Task added successfully"}), 201
