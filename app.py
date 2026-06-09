from flask import Flask, request, jsonify
from dataManager import dataManager

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    
    sent_data = request.json
    username = sent_data["username"]
    password = sent_data["password"]


    
    user_data = dataManager.read("data.json")

    
    for id, data in user_data.items():
        if data["name"] == username and data["password"] == password:
            return jsonify({"success" : True, "user_data" : data})
    return jsonify({"success" : False})


@app.route("/register", methods=["POST"])
def register():
    
    sent_data = request.json
    username = sent_data["username"]
    password = sent_data["password"]

    forbidden_chars = [" ", ".", ",", ";", ":", "[", "]", "(", ")", "{", "}", "&", "%", "$", "!", "/", "=", "?", "#", "<", ">", "|", "+", "-", "ä", "Ä", "ö", "Ö", "ü", "Ü"]

    user_data = dataManager.read("data.json")

    for id, data in user_data.items():
        for char in username:
                if char in forbidden_chars:
                    return jsonify({"success" : False, "message" : "Username contains forbidden characters!"})
                
        if len(username) > 20:
            return jsonify({"success" : False, "message" : "Username is too long!"})
        if not username:
            return jsonify({"success" : False, "message" : "Username cannot be empty!"})        
        if data["name"] == username:
            return jsonify({"success" : False, "message" : "Username already exists!"})
        
        if not password:
            return jsonify({"success" : False, "message" : "Password cannot be empty!"})
        if len(password) < 4:
            return jsonify({"success" : False, "message" : "Password is too short!"})
    user_data[len(user_data)+1] = {
        "name" : username,
        "password" : password,
        "birth_date" : "",
        "note" : "",
        "mode" : "dark",
        "logged_in" : True,
        "disabled" : False,
        "deleted" : False,
        "removed_features" : [],
        "admin" : False,
        "last_change" : ["registered", ""]
        }
        
    dataManager.write("data.json", user_data)
    return jsonify({"success" : True, "message" : "User registered successfully!"})

@app.route("/export", methods=["GET"])
def export():

    user_data = dataManager.read("data.json")
    return jsonify(user_data)

@app.route("/read", methods=["POST"])
def read():
    sent_data = request.json
    user_id = sent_data["user_id"]
    user_data = dataManager.read("data.json")
    if user_id in user_data:
        return jsonify({"success" : True, "user_data" : user_data[user_id]})
    return jsonify({"success" : False, "message" : "User not found!"})

@app.route("/write", methods=["POST"])
def write():
    sent_data = request.json
    user_id = sent_data["user_id"]
    updated_data = sent_data["updated_data"]
    user_data = dataManager.read("data.json")
    if user_id in user_data:
        user_data[user_id].update(updated_data)
        dataManager.write("data.json", user_data)
        return jsonify({"success" : True, "message" : "User data updated successfully!"})
    return jsonify({"success" : False, "message" : "User not found!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
