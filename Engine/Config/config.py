import json

class Config:
    def __init__(self, config_file='./Engine/project.json'):
        self.config_file = config_file
        self.config_data = {
            'projects': []
        }
        self.load_config()
        self.ensure_default_keys()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.config_data = json.load(f)
        except FileNotFoundError:
            self.save_config()  # Save the default config if no file exists

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config_data, f, indent=4)

    def get(self):
        return self.config_data.get("projects", [])

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def add_object(self, obj):
        if 'projects' not in self.config_data:
            self.config_data['projects'] = []
        if 'id' not in obj:
            obj['id'] = len(self.config_data['projects']) + 1
        self.config_data['projects'].append(obj)
        self.save_config()

    def update_project_path(self, project_id, new_path):
        for project in self.config_data['projects']:
            if project['id'] == project_id:
                project['path'] = new_path
                break
        self.save_config()
    
    def update_project_name(self,project_id, new_name): 
        for project in self.config_data['projects']: 
            if project['id'] == project_id: 
                project['name'] = new_name
                break
        self.save_config()

    def ensure_default_keys(self):
        if 'projects' not in self.config_data:
            self.config_data['projects'] = []
        self.save_config()