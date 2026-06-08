from flask import Flask, request
from dataManager import dataManager
import json

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    
    data = request.json
    username = data["username"]
    password = data["password"]
    
    with open("data.json", "r") as file:
            user_data = json.load(file)
    #user_data = dataManager.read("data.json")

    for id, data in user_data.items():
        if data["name"] == username and data["password"] == password:
            return {"success" : True, "user_data" : data}
    return {"success" : False}


@app.route("/register", methods=["POST"])
def register():
    
    data = request.json
    username = data["username"]
    password = data["password"]

    forbidden_chars = [" ", ".", ",", ";", ":", "[", "]", "(", ")", "{", "}", "&", "%", "$", "!", "/", "=", "?", "#", "<", ">", "|", "+", "-", "ä", "Ä", "ö", "Ö", "ü", "Ü"]

    user_data = dataManager.read("data.json")

    for id, data in user_data.items():
        for char in username:
                if char in forbidden_chars:
                    return {"success" : False, "message" : "Username contains forbidden characters!"}
                
        if len(username) > 20:
            return {"success" : False, "message" : "Username is too long!"}
        if not username:
            return {"success" : False, "message" : "Username cannot be empty!"}        
        if data["name"] == username:
            return {"success" : False, "message" : "Username already exists!"}
        else:
            if not password:
                return {"success" : False, "message" : "Password cannot be empty!"}
            if len(password) < 4:
                return {"success" : False, "message" : "Password is too short!"}
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
            return {"success" : True, "message" : "User registered successfully!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
