from flask import Flask, request
from dataManager import dataManager

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():

    dataManager.init_data()
    
    data = request.json
    username = data["username"]
    password = data["password"]

    user_data = dataManager.read("data.json")

    for id, data in user_data.items():
        if data["name"] == username and data["password"] == password:
            return {"correct" : True, "user_data" : data}
        else:
            return {"correct" : False}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)