import json 
from pathlib import Path 

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

user_file = data_dir / "users.json"

def load_data(file_path):
    if not file_path.exists():
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    

def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=5)

def load_users():
    return load_data(user_file)

def save_user(user_dict):
    users = load_users()
    users.append(user_dict)
    save_data(user_file, users)