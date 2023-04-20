from flask import jsonify

class CreateDict(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

    def toJson(self):
        result = []
        for k, v in self.items():
            result.append(v)
        return jsonify(result)