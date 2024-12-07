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
    def __init__(self) -> None:
        self.config = ConFig()
        # Fonte de texto padrão
        self.font = pygame.font.Font(None, int(config['Style']['console_font_height']))