from flask import Flask, session, render_template, request, redirect
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# import os

app = Flask(__name__)

# uri = os.getenv("URI")
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client["StandUp"]
# users_collection = db["users"]

# users = users_collection.find({})

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

@app.route("/")
def home():
    # if 'user' in session:
    #         return render_template("groups.html")
    # if request.method == "POST":
    #     name = request.form.get("name")
    #     cell = request.form.get("cell")
    #     try:
    #         for user in users:
    #              if user["name"] == name and user["cell"] == cell:
    #                 print(user)
    #                 session['user'] = user['cell']
    #                 return redirect("/groups")
    #     except Exception as e:
    #         return f"Failed to login: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)