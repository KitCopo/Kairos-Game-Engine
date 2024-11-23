import json

class ConFig:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_data = {
            'window_size': [1000, 600],
            'project_data': True,
            'project_select': [],
            'chat_local': []
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
    
    def addMensageBank(self,type,mensage):
        if type not in ('Kairos','Mensage','Error','Warning'):
            print('tipo de mensagem invalido')
            return
        
        menssage = { 
            'type': type,
            'mensage': mensage
        }
        self.config_data['chat_local'].append(menssage)
        self.save_config()
    
    def ClearBuffers(self): 
        self.config_data['chat_local'] = []
        self.save_config()
    
    def set_project_name(self, new_name):    
            self.config_data['project_select'] = [new_name]
            print(self.config_data['project_select'])
            self.save_config()
        
    def get_project_name(self):
        project_name = self.config_data['project_select'][0]['name']
        return project_name
    
    def get_project_path(self): 
        project_path = self.config_data['project_select'][0]['path']
        return project_path
    
    def add_project_data(self, value):
        if isinstance(value, bool):  # Verifica se o valor é um booleano
            self.config_data['project_data'] = value
            self.save_config()
        else:
            raise ValueError("O valor deve ser um booleano (True ou False)")
        
    def get_project_data(self):
        return self.config_data.get('project_data', False)

    def ensure_default_keys(self):
        if 'window_size' not in self.config_data:
            self.config_data['window_size'] = [1000, 600]
        if 'project_data' not in self.config_data:
            self.config_data['project_data'] = True
        if 'project_select' not in self.config_data:
            self.config_data['project_select'] = []
        if 'chat_local' not in self.config_data:
            self.config_data['chat_local'] = []
        self.save_config()