import json
import os
import pathlib

_file_name=f"{pathlib.Path(__file__).parent.resolve()}/users.json"

def read_json():
    if not os.path.isfile(_file_name):
        with open(_file_name, 'w') as file:
            json.dump([], file)
    with open(_file_name, 'r') as file:
        users = json.load(file)
    return users

def write_json(new_data):
    with open(_file_name, 'w') as file:
        json.dump(new_data, file)