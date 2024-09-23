import json

def register():
    return "open_interpreter_launcher"

def load_profile(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def save_profile(config_file, profile):
    with open(config_file, 'w') as f:
        json.dump(profile, f)

def quick_setup(config_file):
    # 简化版实现
    default_config = {"language": "python", "timeout": 60}
    save_profile(config_file, default_config)

def run():
    return {
        "load_profile": load_profile,
        "save_profile": save_profile,
        "quick_setup": quick_setup
    }

