# Imports
import json
import os

class File:
    def __init__(self, filename, default="No Value"):
        self.filename = filename + ".json"
        self.default = default

        self.check()

    def check(self): # File Exists/Empty Check
        try: 
            with open(self.filename, encoding="utf-8", mode="r+") as f:
                if f.read() == "": # If File Empty, Set To Default Value
                    json.dump(self.default, f)
        except FileNotFoundError: # If File Doesn't Exist, Create File With Default Value
            with open(self.filename, encoding="utf-8", mode="w+") as f:
                json.dump(self.default, f)

    def save(self, value): #
        self.check()

        with open(self.filename, encoding='utf-8', mode="w") as f:
            json.dump(value, f)

    def get(self):
        with open(self.filename, encoding='utf-8', mode="r") as f:
            return json.load(f)
    
    def __repr__(self):
        with open(self.filename, encoding='utf-8', mode="r") as f:
            return json.load(f)
    
    def delete(self):
        os.remove(self.filename)
