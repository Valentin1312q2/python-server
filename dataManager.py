import json
import os

class dataManager:
    def __init__(self):
        pass

    def init_data():
        appdata = os.getenv("APPDATA")
        main_folder = os.path.join(appdata,"programms_by_v")
        programm_folder = os.path.join(main_folder,"Userprogramm")

        if not os.path.exists(main_folder):
            os.makedirs(main_folder)
        if not os.path.exists(programm_folder):
            os.makedirs(programm_folder)

        user_data = os.path.join(programm_folder,"data.json")

        
        if not os.path.exists(user_data):
            with open(user_data, "w") as f:
                f.write("{}")

        modes_data = {
    "dark" : {
        "window" : "#23272b",
        "main_frame" : "#191c1f",
        "frame" : "#141618",
        "text" : "#fff",
        "text2" : "#bababa"
    },
    "light" : {
        "window" : "#d9d9d9",
        "main_frame" : "#a8a8a8",
        "frame" : "#919191",
        "text" : "black",
        "text2" : "#212121"

    }
}
        
        modes = os.path.join(programm_folder,"modes.json")

        with open(modes, "w") as f:
                json.dump(modes_data, f, indent=4)

    def read(f):
        appdata = os.getenv("APPDATA")
        main_folder = os.path.join(appdata,"programms_by_v")
        programm_folder = os.path.join(main_folder,"Userprogramm")

        with open(f"{programm_folder}/{f}", "r") as file:
            return json.load(file)
        
    def write(f, data):
        appdata = os.getenv("APPDATA")
        main_folder = os.path.join(appdata,"programms_by_v")
        programm_folder = os.path.join(main_folder,"Userprogramm")

        with open(f"{programm_folder}/{f}", "w") as file:
            json.dump(data, file, indent=4)