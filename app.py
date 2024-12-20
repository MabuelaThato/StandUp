from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from flask import Flask,request,jsonify
import os, datetime
# from twilio.rest import Client
# from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

uri = os.environ.get("URI")
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["StandUp"]
users_collection = db["Users"]
groups_collection = db["groups"]
tasks_collection = db["tasks"]

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://stand-up-frontend-ten.vercel.app'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name')
    cell = data.get('cell')
    try:
        user = db["Users"].find_one({"name": name, "cell": cell})
        if user:
            return user
    except Exception as e:
        return {"failed to get users": e}

# @app.route('/groups', methods=['GET'])
# def get_groups():
#     user_cell = request.args.get('user_cell')
#     try:
#         groups = list(db["groups"].find({"members": user_cell}))
#     except Exception as e:
#         return jsonify({"error": e})
    
#     for group in groups:
#         group['_id'] = str(group['_id'])
#     return jsonify(groups), 200


# @app.route('/groups', methods=['POST'])
# def add_group():
#     data = request.json
#     project_name = data.get('project-name')
#     members = data.get('members')
#     members_info = []
#     try:
#         users = list(db["users"].find({}))
#     except Exception as e:
#         return jsonify({"error": e})
    
#     for user in users:
#         if user["name"] in members:
#             members_info.append(user)
#     date = datetime.datetime.now()
#     new_group = {"name": project_name, "members": members, "created_date": date}
#     load_dotenv() 
#     account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
#     auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
#     client = Client(account_sid, auth_token)

#     try:
#         db["groups"].insert_one(new_group)
#         for member in members_info:
#             cell = member[cell]
#             cell[0] = "+27"
#             message = client.messages.create(
#                 body=f"You have been added to group {project_name}. Your group members are {members}",
#                 from_=os.environ.get("TWILIO_NUMBER"),
#                 to = cell,
#                 )
#             print(message.body)
#         return jsonify({"message": "Group created successfully"}), 201
#     except Exception as e:
#         return jsonify({"error": e})
    
# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     group_id = request.args.get('group_id')
#     try:
#         tasks = list(db["tasks"].find({"group_id": group_id}))
#     except Exception as e:
#         return jsonify({"error": e})
#     for task in tasks:
#         task['_id'] = str(task['_id'])
#     return jsonify(tasks), 200

# @app.route('/tasks', methods=['POST'])
# def add_task():
#     data = request.json
#     group_id = data.get('group_id')
#     task_name = data.get('name')
#     assigned_to = data.get('assigned_to')
#     date = datetime.datetime.now()
    
#     new_task = {"group_id": group_id, "name": task_name, "assigned_to": assigned_to, "created_date": date, "status": "not started"}
#     try:
#         db["tasks"].insert_one(new_task)
#     except Exception as e:
#         return jsonify({"error":e})
#     return jsonify({"message": "Task added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
