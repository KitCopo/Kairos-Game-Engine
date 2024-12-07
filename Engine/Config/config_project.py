import json
import os

class ProjectConfig:
    def __init__(self, project_path):
        self.project_path = project_path
        self.config_file = os.path.join(project_path, 'configs', 'config.json')
        self.config_data = {
            'main_scene': True,
            'objects': [],
            'last_index': 0,  # Campo para rastrear o último índice
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

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()
    
    def get_state_mainSceen(self) -> bool: 
        state = self.config_data['main_scene']
        return state

    def change_mainSceen_state(self,state): 
        self.config_data['main_scene'] = state
        self.save_config()

    def add_object(self, obj):
        # Adiciona o objeto com o índice atual
        obj['indece'] = self.config_data['last_index']
        self.config_data['objects'].append(obj)
        self.config_data['last_index'] += 1
        self.save_config()
    
    def change_visible_obj(self,obj_id):
        objects = self.config_data.get('objects', [])
        for obj in objects: 
            if obj.get('indece') == obj_id:
                obj['visible_in_sceen'] = not obj.get('visible_in_sceen', False)
        
        self.save_config()
        
    def delete_object(self, obj_id):
        objects = self.config_data.get('objects', [])
        new_objects = [obj for obj in objects if obj.get('indece') != obj_id]

        # Atualiza o last_index se necessário
        if obj_id == self.config_data['last_index'] - 1:
            if new_objects:
                self.config_data['last_index'] = max(obj.get('indece') for obj in new_objects) + 1
            else:
                self.config_data['last_index'] = 0

        self.config_data['objects'] = new_objects
        self.save_config()

    def get_objects(self):
        return self.config_data.get('objects', [])
        
    def ensure_default_keys(self):
        if 'objects' not in self.config_data:
            self.config_data['objects'] = []
        if 'last_index' not in self.config_data:
            self.config_data['last_index'] = 0
        self.save_config()
