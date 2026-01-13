import json
import os

def load_json(file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "test-data", file_name)

    with open(file_path, "r") as f:
        return json.load(f)