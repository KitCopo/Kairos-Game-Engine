#console Version 0.0.1
#include Debug , Errors , Alerts , Mensagens
import os
import configparser
import pygame
from Config.config_engine import *

pygame.init()
config_file_path = os.path.join(os.path.dirname(__file__), 'configs.ini')

config = configparser.ConfigParser()
if os.path.exists(config_file_path):
    config.read(config_file_path)
else:
    print(f"Config file {config_file_path} not found!")


class Console:
    def __init__(self, window: pygame.Surface,data_objs) -> None:
        self.window = window
        self.config = ConFig()
        self.Chat_local = self.config.get('chat_local', [])
        self.data_objs = data_objs
        # Fonte de texto padrão
        self.font = pygame.font.Font(None, int(config['Style']['console_font_height']))
        
    def Show(self) -> None:
        self.data_objs.update_size_position()
        data_objs_size = self.data_objs.Size
        self.Size = [self.window.get_width() - data_objs_size[0] - 2, int(self.window.get_height() * 0.25)]
        self.Vec = [0,self.window.get_height() - self.Size[1]]
        self.img_error_pos = (self.Vec[0] + 10, self.Vec[1] + 50)
        y_offset = self.Vec[1] + 35
        background_color = (20,20,20)
        pygame.draw.rect(self.window, background_color, (self.Vec[0] + 3,self.Vec[1] + 25,self.Size[0] - 6,self.Size[1] - 30),border_radius=5)
        for message in self.Chat_local:
            # Define cor de texto e ícone
            color = (200, 200, 200) if message['type'] == 'Mensage' else (255, 165, 0) if message['type'] == 'Warning' else (255, 0, 0) if message['type'] == 'Error' else (150,150,150)
            
            # Exibe o ícone ao lado da mensagem
            # Renderiza o texto
            text_surface = self.font.render(message['mensage'], True, color)

            self.window.blit(text_surface, (self.Vec[0] + 10 , y_offset))
            
            y_offset += text_surface.get_height() + 5  # Espaçamento entre mensagens
    
    def addMensageBank(self, type: str, user_mensage: str) -> None:
        self.config.addMensageBank(type,user_mensage)
    
    def ClearBuffers(self) -> None:
        self.config.ClearBuffers()
        
