import json
from os import path

class Config:
    def __init__(self, disabled_modules):
        self.disabled_modules = disabled_modules

    def save(self):
        with open("config.json", "w") as f:
            f.write(json.dumps({"disabled_modules": self.disabled_modules}, indent=4))

    def load():
        if path.exists("config.json"):
            return Config(**json.loads(open("config.json").read()))
        else:
            return Config([])