import json
import os

class dataManager:
    def __init__(self):
        pass

    
    def read(f):
        
        with open(f"{f}", "r") as file:
            return json.load(file)
        
    def write(f, data):
        with open(f"{f}", "w") as file:
            json.dump(data, file, indent=4)